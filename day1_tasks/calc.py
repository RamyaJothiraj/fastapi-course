from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
    return {"Status":"FastAPI is running..."}
@app.get("/calc")

def calc(n1 :int ,n2: int,op: str):
    ops={
        '+': n1+n2,
        '-': n1-n2,
        '*' : n1*n2,
        '/': n1/n2
    }
    if op not in ops:
        return {"error":"Invalid operation"}
    if op == '/' and n2 == 0:
        return {"error_msg":"cannot be divisible by 0..."}
    
    return {"Result":ops[op]}