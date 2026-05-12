from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def home():
    return {"msg":"Movie ticket booking FastAPI is running..."}

@app.get("/movie")

def movie(movie_name:str):
    if movie_name == "Leo":
        return {
            "timings": "15:00 pm",
            "ratings": "4.8 stars",
            "language" : "Tamil"
        }
    elif  movie_name  == "Vikram":
        return {
            "timings": "19:00 pm",
            "ratings": "4.5 stars",
            "language" : "Tamil"
        }
    elif movie_name == "Avengers":
        return {
            "timings": "9:00 am",
            "ratings": "4.8 stars",
            "language" : "English"
        }
    else:
        return {"Invalid movie_name":"Enter correct movie name..."}

@app.get("/ticket-price")

def ticket_calculation(tickets:int,seat:str):
    seat_type ={
        "Premium":240,
        "Normal":180,
        "Front":90
    }
    if seat not in seat_type:
        return {"Error":"Invalid seat type"}
    tot = tickets*seat_type[seat]
    return {
        "seat_type":seat,
        "Price":seat_type[seat],
        "Tickets":tickets,
        "Total":tot
    }
@app.get("/age-valid")

def age_validation(age:int):
    if  age < 18 : return {"Status":"Not valid"}
    else: return{"Status":"Valid"}

@app.get("/snack-order")

def  snacks(popcorn_qty:int=0,popcorn_size:str="Small",cool_drinks:int=0,ice_cream:int=0):
    popcorn_prices = {
        "Large":180,
        "Medium":90,
        "Small":70
    }

    if popcorn_size not in popcorn_prices:
        return {"Error":"Incorrect Quantity..."}
    
    # individual  qty
    popcorn_tot = popcorn_qty*popcorn_prices[popcorn_size]
    ice_cream_tot = ice_cream * 90
    cool_drink_tot = cool_drinks * 40
    
    # # both popcorn and drinks
    combo_drinks = popcorn_tot+cool_drink_tot
    combo_ice_creams = popcorn_tot+ice_cream_tot

    # grand total
    total = (popcorn_tot+cool_drink_tot+ice_cream_tot)
    response = {}

    if popcorn_qty > 0:
        response["Popcorn"] =  {
            "quantity": popcorn_qty,
            "size": popcorn_size,
            "total": popcorn_tot
        }
    if cool_drinks > 0:
        response["CoolDrinks"] =  {
            "quantity": cool_drinks,
            "total": cool_drink_tot
        }
        
    if ice_cream > 0:
        response["Ice Creams"] =  {
            "quantity": ice_cream,
            "total": ice_cream_tot
        }
    if  cool_drinks > 0 and popcorn_qty >0:
        response["Combo1"] = {
            "Combo1":"Pepsi+Popcorn combo",
            "Price": combo_drinks
        }
    if  ice_cream > 0 and popcorn_qty >0:
        response["Combo2"] = {
            "Combo2":"Ice  cream + Popcorn combo",
            "Price": combo_ice_creams
        }
    response["Grand total"] = total
    return response
@app.get("/admin-login")

def login(admin_name:str,password:str):
    if admin_name == "admin" and password == "movies123":
        return {"Status":"Success!!"}
    else: return {"Status":"Invalid credentials..."}

@app.get("/welcome")
def welcome(name:str|None=None):
    if name:
        return {"Greeting":f"Welcome {name}"}
    return {"Greeting":"Welcome Guest!!"}
