from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
    return {"msg":"API is running..."}

@app.get("/number-analyser")

def num_analyser(n:int):
    is_even =True if(n%2==0) else False
    is_positive = True if (n>0) else False
    square = n*n

    return {
        "is_even":is_even,
        "is_positive":is_positive,
        "square": square
    }