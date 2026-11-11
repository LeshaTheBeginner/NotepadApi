from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
# import timestamp as tp

class NoteObj(BaseModel):
    noteid: UUID
    notename: str
    noteowner: str
    notedata: str
    notetype: str
    favorite: bool
    notecreatedate: datetime
    noteeditdate: datetime