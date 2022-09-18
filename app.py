from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello world"}

@app.post("/hook")
async def hook(request: Request) -> dict:
    """ accept webhook"""
    print(dir(request))
    print(request.json())
    return {"Message": "successfully registerd"}


@app.get("/name")
async def get_name(request: Request) -> dict:
    """ return name """
    print(request.base_url)
    return {"name": "prabal pathak"}
