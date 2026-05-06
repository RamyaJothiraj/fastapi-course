from fastapi import FastAPI

app = FastAPI()

@app.get("/home")

def home():
    return {"msg":"Hi"}

@app.get("/hello")

def hello():
    return {"message":"Hello from Razz^-^"}

@app.get("/about")

def about():
    return {"info":"My first FastAPI app"}
