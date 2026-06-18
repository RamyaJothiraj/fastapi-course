from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
    return {
        "status":"API running..."
    }
@app.get("/tables/{num}")
def table(num:int):
    res = []

    for i in range(1,11):
        res.append(f"{num}x{i}={num*i}")
    return {
        "Tables": res
    }
@app.get("/BMI/{height}/{weight}")
def BMI(height:float,weight:float):
    return {
        "category":(weight)/(height*height)
    }
@app.get("/bill/{units}")
def bill(units:int):
    amt = 0
    for unit in range(1,units+1):
        if unit  <= 100: amt+=5
        elif unit <= 200: amt+=7
        else:  amt+=10
    return {
        "units":units,
        "amount":amt
    }
@app.get("/password/{pwrd}")
def password(pwrd:str):
    has_num = False
    for ch in pwrd:
        if ch.isdigit():
            has_num = True
            break
    if len(pwrd) >= 8 and has_num:
        return {
            "password":pwrd,
            "strength":"Strong"
        }
    return {
        "password":pwrd,
        "Strength":"Weak"
    }
        