from fastapi import FastAPI
app = FastAPI()

@app.get("/")

def home():
    return {"msg":"FastAPI is running..."}
@app.get("/login")
def login(username:str,password:str):
    if (username == "admin" and password == "abc@123"): 
        return {"status":"Login successful..."}
    return {"status":"Invalid credentials... Plz  try again later!!"}
