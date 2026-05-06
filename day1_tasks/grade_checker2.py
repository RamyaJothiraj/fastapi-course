from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
    return {"Status":"FastAPI is running..."}
@app.get("/grade")

def grade(mark:int):
    if mark > 100 or mark < 0:
        return {"error":"Invalid marks"}
    elif mark >= 90 :
        return {"Grade":"A"}
    elif  mark >= 75 :
        return {"Grade":"B"}
    elif  mark >= 50 :
        return {"Grade":"C"}
    else:
        return {"Grade ":"D"}