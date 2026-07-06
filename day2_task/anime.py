from fastapi import FastAPI
app = FastAPI()

anime = [
    "Naruto",
    "AOT",
    "Jujutsu Kaisen",
    "Berserk",
    "Full metal Alchemist"
]
@app.get("/")
def home():
    return {"msg":"FastAPI is running..."}
@app.get("/anime")
def get_anime():
    return {
        "Anime":anime
    }
@app.get("/anime/anime-count")
def total_count():
    return {
        "Anime count": len(anime)
    }
@app.get("/anime/search/{name}")
def search_name(name:str):
    for s in anime:
        if s.lower() == name.lower():
            return {
                "Status":"Found",
                "Anime":s
            }
    return {
        "Error":"Invalid"
    }
@app.get("/anime/anime-index/{num}")
def count_using_index(num:int):
    if 0 <= num < len(anime):
        return {
            "Anime":anime[num]
        }
    else:
        return {
            "Error":"Invalid"
        }
@app.get("/anime/anime-first")
def first_anime():
    return {
        "First Anime": anime[0]
    }
@app.get("/anime/anime-last")
def last_anime():
    return {
        "Last Anime": anime[-1]
    }
