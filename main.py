from fastapi import FastAPI, HTTPException, Query
from airtable_client import get_random_fact

app = FastAPI(title="Public Trivia API")

@app.get("/fact/random")
def random_fact(category: str = Query(None)):
    fact = get_random_fact(category)
    if not fact:
        raise HTTPException(status_code=404, detail="Uh oh! No fact found")
    return fact
