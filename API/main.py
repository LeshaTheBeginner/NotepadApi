import sys 
from pathlib import Path
Database_PATH = Path(__file__).resolve().parent.parent / "Database"
sys.path.append(str(Database_PATH))
# import timestamp as tp


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
from note_dataclasses import createNotes
from model import engine,noteTable,metadata
from schema import NoteObj
import sqlalchemy
import uvicorn
from pprint import pprint  


connection = engine.connect()

app = FastAPI()

#qfavorite = sqlalchemy.select(noteTable).where(noteTable.columns.favorite == True)
#qnewest = sqlalchemy.select(noteTable).order_by(noteTable.columns.notecreatedate)
#qcreatenew = sqlalchemy.insert(noteTable).values(noteowner='test.py',notedata='Test for test.py inserting with code',favorite=True,)
#qselect = sqlalchemy.select(noteTable).where(noteTable.columns.noteid == "799f6e39-b28e-4c57-a66f-7d20ef705a6c")

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/help")
async def help():
    return {"message": "help page but he have none"}

@app.post("/create",response_model=str)
async def createNote(item:createNotes):
    qcreatenew = sqlalchemy.insert(noteTable).values(noteowner=item.noteowner,notename=item.notename,notedata=item.notedata,notetype=item.notetype)
    result_proxy = connection.execute(qcreatenew)
    connection.commit()
    return "Thank you for creating a note!"

@app.get("/edit")
async def root():
    return {"message": "Hello World"}

@app.get("/delete")
async def root():
    return {"message": "Hello World"}

@app.get("/getnotes",response_model=list[NoteObj])
async def getnotes():
    qnewest = sqlalchemy.select(noteTable).order_by(noteTable.columns.notecreatedate)
    result_proxy = connection.execute(qnewest)
    result_set = result_proxy.fetchall()
    pprint(result_set)
    return result_set

@app.get("/star")
async def root():
    return {"message": "Hello World"}

@app.get("/lastused")
async def root():
    return {"message": "Hello World"}

@app.get("/lastcreated")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    # Run the server using Uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
