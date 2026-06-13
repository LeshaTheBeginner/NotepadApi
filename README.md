# NotepadApi
/create -- Creates a note
/edit -- Edits a note
/delete -- Deletes a note
/getnotes Returns all the notes
/star Stars (Favorites) a note
/lastcreated Returns the last created note
/lastused -- Returns the last used note
/help -- Help Page
/ -- Hello World!


# Database config/structure
noteid = uuid DEFAULT gen_random_uuid()
notename = VARCHAR(255)
noteowner = VARCHAR(32)
notedata = TEXT NOT NULL
notetype = VARCHAR(8)
favorite = BOOLEAN
notecreatedate = TIMESTAMP
noteeditdate = TIMESTAMP
