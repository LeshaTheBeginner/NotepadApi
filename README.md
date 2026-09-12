# NotepadApi
/create - POST - Creates a note
/edit - POST - Edits a note
/delete - POST - Deletes a note
/getnotes - GET - Returns all the notes
/star - POST - Stars (Favorites) a note
/lastcreated - GET - Returns the last created note
/lastused - GET - Returns the last used note
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
