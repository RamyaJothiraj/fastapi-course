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