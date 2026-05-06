from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
    return {"Status":"FastAPI is running..."}
@app.get("/grade")

def grade(mark:int):
    grade_map = {
        range(90,101) : 'A',
        range(75,90) : 'B',
        range(50,75) :'C',
        range(0,50):'D'
    }

    for mark_range,grade_val in grade_map.items():
        if mark in mark_range:
            return {"Grade":grade_val}
    return {"error":"Invalid marks"}