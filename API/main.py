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
# noteid=0 notename = DELETED
# /lastcreated
# /lastused
# /search
# /copy
# /help
# /
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from note_dataclasses import *
from model import engine,noteTable,metadata
from schema import NoteObj
import sqlalchemy
import uvicorn
import uuid
from datetime import datetime

connection = engine.connect()

app = FastAPI()

#qfavorite = sqlalchemy.select(noteTable).where(noteTable.columns.favorite == True)
#qnewest = sqlalchemy.select(noteTable).order_by(noteTable.columns.notecreatedate)
#qcreatenew = sqlalchemy.insert(noteTable).values(noteowner='test.py',notedata='Test for test.py inserting with code',favorite=True,)
#qselect = sqlalchemy.select(noteTable).where(noteTable.columns.noteid == "799f6e39-b28e-4c57-a66f-7d20ef705a6c")

@app.get("/")
async def root():
    return {"message": "Hello World! add /help to get the commands and such"}

@app.get("/help", response_class=HTMLResponse)
async def help():
    return ''' <h1>NotepadApi - Made by LeshaTheBeginner (<a href="https://github.com/LeshaTheBeginner/NotepadApi">GitHub</a>)</h1>
<p>/create - POST - Creates a note. This is the structure: {"noteowner":"yourNameHere","notename":"noteName","notedata":"theNoteStuffInHere","notetype":"mdOrTxtThisIsForTheFuture"}</p>
<p>/edit - POST - Edits a note. Basically you can edit notename and/or notedata and/or notetype. Same structure as before</p>
<p>/delete - POST - Deletes a note (and permamently deletes the last note it called twice). Requires a UUID of the note, there can only be one recoverable/perm delatable note with UUID 0.</p>
<p>/getnotes/{n} - GET - Returns all the notes with 10 notes in each page ({n} = page number)</p>
<p>/star - POST - Stars (Favorites) a note. Requires note's UUID</p>
<p>/lastdeleted - GET - Returns the last deleted note</p>
<p>/lastcreated - GET - Returns the last created note</p>
<p>/lastused - GET - Returns the last used </p>
<p>/search - POST - Returns notes based on search query</p>
<p>/copy - POST - Duplicates a note with a new UUID</p>
<p>/recover - GET - Recovers the last deleted note</p>
<p>/help - GET - Help Page</p>
<p>/ - GET - Hello World!</p>
<p>Whoever finds this, i mean do whatever you want ot do here as long as you don't delete everything.</p>
<p>Rules are:</p>
<p>don't delete everything</p>
<p>be normal\n</p>
<p>Done</p>
'''

@app.post("/create",response_model=str)
async def createNote(item:createNotes):
    qcreatenew = sqlalchemy.insert(noteTable).values(noteowner=item.noteowner.encode("unicode-escape").decode()
                                                    ,notename=item.notename.encode("unicode-escape").decode()
                                                    ,notedata=item.notedata.encode("unicode-escape").decode()
                                                    ,notetype=item.notetype.encode("unicode-escape").decode())
    result_proxy = connection.execute(qcreatenew)
    connection.commit()
    return "Thank you for creating a note!"

@app.post("/edit",response_model=str)
async def editNote(item:editNotes):
    qselect = sqlalchemy.select(noteTable).where(noteTable.columns.noteid==item.noteid)
    result_proxy = connection.execute(qselect)
    temp_list = result_proxy.fetchall()
    qedit = sqlalchemy.update(noteTable).values(notename=item.notename.encode("unicode-escape").decode() if item.notename else temp_list[0][1]
                                                ,notedata=item.notedata.encode("unicode-escape").decode() if item.notedata else temp_list[0][3]
                                                ,notetype=item.notetype.encode("unicode-escape").decode() if item.notetype else temp_list[0][4]
                                                ,noteeditdate=datetime.now()).where(noteTable.columns.noteid==item.noteid)
    result_proxy = connection.execute(qedit)
    connection.commit()
    return f"Successfully edited the note with UUID {str(temp_list[0][0])} !"

@app.post("/delete",response_model=str)
async def notedelete(item:selectNotes):
    #if item.noteid != 0
    deletedid = UUID(int=0)
    qselect = sqlalchemy.select(noteTable).where(noteTable.columns.noteid==item.noteid)
    qdelete = sqlalchemy.delete(noteTable).where(noteTable.columns.noteid==deletedid)
    qfakedelete = sqlalchemy.update(noteTable).where(noteTable.columns.noteid==item.noteid).values(noteid=deletedid,notecreatedate=datetime.now())
    deletedNote = connection.execute(qselect)
    request = deletedNote.fetchall() # FUCK YOU MEAN '[]' DAWG
    result_proxy = connection.execute(qdelete) # If it doesnt find anything, nothing happens
    result_proxy = connection.execute(qfakedelete) 
    connection.commit()
    return f"Removed {request} ."

@app.get("/getnotes/{page_id}",response_model=list[NoteObj])
async def getnotes(page_id = 1):
    #FEATURE: PAGINATE THIS SO IT WOULD BASICALLY SHOW ONLY OF UP TO 50 CHARACTERS OF CONTENTS OF EACH NOTE
    page_id = int(page_id) if int(page_id) >= 1 else 1
    qnewest = sqlalchemy.select(noteTable).order_by(sqlalchemy.desc(noteTable.columns.notecreatedate)).offset(int((page_id-1)*10)).limit(10)
    result_proxy =  connection.execute(qnewest)
    result_set = result_proxy.fetchall()
    return result_set

@app.post("/star",response_model=str)
async def notestar(item:selectNotes):
    qselect = sqlalchemy.select(noteTable).where(noteTable.columns.noteid==item.noteid)
    result_proxy = connection.execute(qselect)
    selected = result_proxy.fetchall()
    qfavorite = sqlalchemy.update(noteTable).values(favorite=not selected[0][5]).where(noteTable.columns.noteid==item.noteid)
    result_proxy = connection.execute(qfavorite)
    connection.commit()
    return "Successfully Favorited/Unfavorited!"

@app.get("/lastused",response_model=NoteObj)
async def getlastused():
    qnewest = sqlalchemy.select(noteTable).order_by(noteTable.columns.noteeditdate)
    result_proxy =  connection.execute(qnewest)
    result_set = result_proxy.fetchall()
    return result_set[-1]

@app.get("/lastcreated",response_model=NoteObj)
async def getlastcreated():
    deletedid = UUID(int=0)
    qnewest = sqlalchemy.select(noteTable).order_by(noteTable.columns.notecreatedate).where(noteTable.columns.noteid!=deletedid)
    result_proxy = connection.execute(qnewest)
    result_set = result_proxy.fetchall()
    return result_set[-1]

@app.post("/search",response_model=list[NoteObj])
async def searchnotes(search:searchNotes): #{"aaaaaa8492734820":"testname","aaaaaa8492734820":"testname","aaaaaa8492734820":"testname"} print("te" in i)
    qsearch = sqlalchemy.select(noteTable).where(noteTable.columns.notename.icontains(str(search.search_query))) # icontains = case insensitive contains, contains = case sensitive contains
    result_proxy = connection.execute(qsearch)
    result_set = result_proxy.fetchall()
    return result_set

@app.post("/copy", response_model=str)
async def copynote(item:selectNotes):
    qselect = sqlalchemy.select(noteTable).where(noteTable.columns.noteid==item.noteid)
    result_proxy = connection.execute(qselect)
    selected = result_proxy.fetchall()
    duplicate = sqlalchemy.insert(noteTable).values(noteowner=selected[0][2],notename=selected[0][1],notedata=selected[0][3],notetype=selected[0][4],favorited=selected[0][5])
    result_proxy = connection.execute(duplicate)
    connection.commit()
    return "Successfully Duplicated!"

@app.get("/lastdeleted", response_model=str)
async def lastdeleted():
    deletedid = UUID(int=0)
    qselect = sqlalchemy.select(noteTable).where(noteTable.columns.noteid==deletedid)
    result_proxy = connection.execute(qselect)
    try:
        selected = result_proxy.fetchall()[0]
    except:
        return "Can't find the last deleted note. Was it permanently deleted?"
    return selected

@app.get("/restore", response_model=str)
async def restore():
    deletedid = UUID(int=0)
    qdelete = sqlalchemy.delete(noteTable).where(noteTable.columns.noteid==deletedid)
    qrestore = sqlalchemy.select(noteTable).where(noteTable.columns.noteid==deletedid)
    result_proxy = connection.execute(qrestore)
    try:
        result_note = result_proxy.fetchall()[0]
    except IndexError:
        return "Nothing to restore!"
    qcreatenew = sqlalchemy.insert(noteTable).values(notename=result_note[1],noteowner=result_note[2],notedata=result_note[3],notetype=result_note[4])
    result_proxy = connection.execute(qcreatenew)
    result_proxy = connection.execute(qdelete)
    connection.commit()
    #(UUID('00000000-0000-0000-0000-000000000000'), 'TERMUXTEST', 'termux', 'удаляем', 'txt', False, datetime.datetime(2026, 10, 5, 7, 48, 14, 927798), datetime.datetime(2026, 10, 5, 6, 41, 10, 227450))
    return "Successfully Restored!"



if __name__ == "__main__":
    # Run the server using Uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000,proxy_headers=True)#ssl_keyfile="../../certs/key.pem", ssl_certfile="../../certs/cert.pem") # USE http://127.0.0.1:8000/ ,  0.0.0.0 IS NOW BROKEN
