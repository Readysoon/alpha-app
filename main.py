

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def hello_fly():
    return 'hel from fly.io'


