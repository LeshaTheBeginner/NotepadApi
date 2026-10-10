from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class createNotes(BaseModel):
    notename: str
    noteowner: str
    notedata: str
    notetype: str

class selectNotes(BaseModel):
    noteid: UUID

class editNotes(BaseModel):
    noteid: UUID
    notename: Optional[str] = None
    notedata: Optional[str] = None
    notetype: Optional[str] = None
class searchNotes(BaseModel):
    search_query: str