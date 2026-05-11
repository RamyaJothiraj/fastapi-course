from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"msg":"API is running..."}
@app.get("/fizzbuzz")
def  fizzBuzz(n:int):
    if (n%3 ==0 and n%5==0):
        return {"Result":"FizzBuzz"}
    elif (n%3 ==  0):
        return {"Result":"Fizz"}
    elif (n%5 ==0 ):
        return {"Result":"Buzz"}
    else:
        return {"Result":n}