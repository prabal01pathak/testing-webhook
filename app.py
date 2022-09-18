# pprint module
import json
from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello world"}

@app.post("/hook")
async def hook(request: Request) -> dict:
    """ accept webhook"""
    data = await request.json()
    with open("file.json", "w", encoding="utf-8") as _f:
        json.dump(data, _f, indent=4)
    return {"Message": "successfully registerd"}


@app.get("/name")
async def get_name(request: Request) -> dict:
    """ return name """
    print(request.base_url)
    return {"name": "prabal pathak"}
