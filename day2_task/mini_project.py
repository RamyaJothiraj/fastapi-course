from fastapi import FastAPI
app = FastAPI()


movies = [
    {
        "name":"Leo",
        "ratings": 4.8,
        "language":"tamil",
        "review": "Box office Full"
    },
    {
        "name":"Obsessed",
        "ratings": 4.3,
        "language":"English",
        "review": "Hit"
    },
    {
        "name":"Avengers",
        "ratings": 5.0,
        "language":"English",
        "review": "Block buster!!"
    }
]

@app.get("/")
def home():
    return {
        "msg":"Movie-info Api is running..."
    }
@app.get("/movie/{name}")
def movie(name:str):
    for movie in movies:
        if movie["name"].lower() == name.lower():
            return movie
    return {"Error":"Movie not found!"}
@app.get("/ratings/{name}")
def ratings(name:str):
    for movie in movies:
        if movie["name"].lower() == name.lower():
            return {"MOvie":movie["name"],
                    "Ratings":movie["ratings"]}
    return {"Error":"Movie not found!"}

@app.get("/language/{name}")
def language(name:str):
    for movie in movies:
        if movie["name"].lower() == name.lower():
            return {"MOvie":movie["name"],
                    "Language":movie["language"]}
    return {"Error":"Movie not found!"}
@app.get("/reviews/{name}")
def reviews(name:str):
    for movie in movies:
        if movie["name"].lower() == name.lower():
            return {"MOvie":movie["name"],
                    "Reviews":movie["review"]}
    return {"Error":"Movie not found!"}
@app.get("/ticket/{age}")
def ticket(age:int):
    if age >= 18:
        return{"msg":"Eligible to watch"}
    else:
        return {"error":"Check eligibility..."}