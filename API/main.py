# /create POST
# /edit POST
# /delete POST
# /getnotes
# /star
# /lastdeleted
# /lastcreated
# /lastused
# /help
# / 
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/help")
async def help():
    return {"message": "help page but he have none"}

@app.get("/create")
async def root():
    return {"message": "Hello World"}

@app.get("/edit")
async def root():
    return {"message": "Hello World"}

@app.get("/delete")
async def root():
    return {"message": "Hello World"}

@app.get("/getnotes")
async def root():
    return {"message": "Hello World"}

@app.get("/star")
async def root():
    return {"message": "Hello World"}

@app.get("/lastused")
async def root():
    return {"message": "Hello World"}

@app.get("/lastcreated")
async def root():
    return {"message": "Hello World"}



