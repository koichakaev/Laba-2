from fastapi import FastAPI
import wikipedia
from pydantic import BaseModel

app = FastAPI()

class WikiImput(BaseModel):
    name: str
    quantity: int

@app.get("/wiki")
def wiki():
    return wikipedia.search("Bill", results=2)

@app.post("/wikipedia/{name}")
def wikipedia_search(name, quantity: WikiImput):
    return wikipedia.search(name,results=quantity)

@app.post("/viki/{name}")
def wikipedia_suggest(name: str):
    return wikipedia.suggest(name)