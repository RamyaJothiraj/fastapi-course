from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"msg":"Api is running..."}

@app.get("/interest")
def simp_interest_calc(p:float,r:float,t:float):
    res =(p*r*t)/100 
    return  {"Simple_interest":res}
