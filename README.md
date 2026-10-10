# NotepadApi
/create - POST - Creates a note
/edit - POST - Edits a note
/delete - POST - Deletes a note (and permamently deletes the last note it called twice)
/getnotes - GET - Returns all the notes
/star - POST - Stars (Favorites) a note
/lastdeleted - GET - Returns the last deleted note
/lastcreated - GET - Returns the last created note
/lastused - GET - Returns the last used 
/search - POST - Returns notes based on search query
/copy - POST - Duplicates a note with a new UUID
/recover - GET - Recovers the last deleted note
/help - GET - Help Page
/ - GET - Hello World!

# Database config/structure
noteid = uuid DEFAULT gen_random_uuid()
notename = VARCHAR(255)
noteowner = VARCHAR(32)
notedata = TEXT NOT NULL
notetype = VARCHAR(8)
favorite = BOOLEAN
notecreatedate = TIMESTAMP
noteeditdate = TIMESTAMP

# 

# Directory Highearchy:
/Database -- has managing of the database, and bridging SQL and Python
