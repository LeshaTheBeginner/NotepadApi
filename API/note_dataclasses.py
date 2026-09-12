from pydantic import BaseModel

class createNotes(BaseModel):
    notename: str
    noteowner: str
    notedata: str
    notetype: str