from fastapi import FastAPI

app=FastAPI()
# num1 :-> addn
@app.get("/addn")

def addn(n1:int, n2:int):
    return {"Result": n1+n2}
#str->greeting
@app.get("/greet")

def greet(name:str):
    return {"Msg":f"Greetings from {name}"}
# optimal params
@app.get("/welcome")

def welcome(name:str|None=None):
    if name: return {"msg":f"Welcome {name}"}
    return {"msg":f"Welcome Guest"}

#num-prob2 :-> square

@app.get("/square")
def square(n:int):
    return {"Result":n*n}