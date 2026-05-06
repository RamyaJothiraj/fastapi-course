from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
    return {"msg":"FastAPI is running..."}
@app.get("/password-checker")

def password_checker(s:str):
    length = len(s)
    if length<5 : return {"strength":"weak"}
    elif  length <=8: return {"strength":"medium"}
    else: return {"strength":"strong"}