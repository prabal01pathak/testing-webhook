from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello world"}

@app.post("/hook")
async def hook(request: Request) -> dict:
    """ accept webhook"""
    print(dir(request))
    return {"Message": "successfully registerd"}


