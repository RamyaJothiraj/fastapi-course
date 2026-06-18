from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"msg":"API is running..."}

@app.get("/cube/{num}")
def cube(num:int):
    return {
        "cube":num*num*num
    }

@app.get("/double/{num}")
def double(num:int):
    return {
        "double": num*2
    }
@app.get("/reverse/{txt}")
def reverse(txt:str):
    return {
        "reverse": txt[::-1]
    }
@app.get("/evenOdd/{num}")
def evenOdd(num:int):
    even = "Even" if num%2==0 else "Odd"
    return {
        "evenOdd":even
    }