from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field
from typing import Optional,Annotated

app = FastAPI()
class Person(BaseModel):
    name : Annotated[str,Field(min_length=2,max_length=30)]
class Expense(BaseModel):
    description:Annotated[str,Field(min_length = 3,max_length = 50)]
    amount : Annotated[float,Field(gt=0)]
    paid_by :Annotated[str,Field(min_length=2,max_length=30)]
class ExpenseRequest(BaseModel):
    people: Annotated[list[Person],Field(min_length=2,max_length=10)]
    expenses: Annotated[list[Expense],Field(min_length=1,max_length=20)]
    note : Optional[str]=None

@app.post("/data")
def expense_splitter(data:ExpenseRequest):
    people_names = [person.name for person in data.people]
    for expense in data.expenses:
        if expense.paid_by not in people_names:
            raise HTTPException(
                status_code = 400,
                detail = "Invalid name"
            )
    total_expense = sum(expense.amount for expense in data.expenses)
    equal_share = total_expense/len(data.people)
    receivers = []
    payers = []
    res = []
    for person in data.people:
        amount_paid = sum(expense.amount for expense in data.expenses if expense.paid_by == person.name)
        balance: float = amount_paid-equal_share
        if balance > 0:
            receivers.append({
                "name":person.name,
                "balance":balance
            })
        elif balance < 0:
            payers.append({
                "name":person.name,
                "balance":-balance
            })
        res.append({
            "paid_by": person.name,
            "amount_paid": amount_paid,
            "balance": balance
        })
    settlements = []
    i=0
    j=0
    while i < len(payers) and j < len(receivers):
        payment = min(
            payers[i]["balance"],receivers[j]["balance"]
        )
        settlements.append({
            "from":payers[i]["name"],
            "to": receivers[j]["name"],
            "amount":payment
        })
        payers[i]["balance"]-=payment
        receivers[j]["balance"]-=payment
        if payers[i]["balance"]==0: i+=1
        if receivers[j]["balance"]==0: j+=1


        
    
    return{
        "total_expense": total_expense,
        "equal_share":equal_share,
        "people":res,
        "received": receivers,
        "paid": payers,
        "settlement":settlements
    }