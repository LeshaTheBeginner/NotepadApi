from pydantic import BaseModel
# import timestamp as tp

class NoteObj(BaseModel):
    noteid: str
    notename: str
    noteowner: str
    notedata: str
    notetype: vars
    favorite: bool
    notecreatedate: str
    noteeditdate: str