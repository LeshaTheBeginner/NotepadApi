# NotepadApi - Made by LeshaTheBeginner ([GitHub](https://github.com/LeshaTheBeginner/NotepadApi"))
## Requests
Requests is the way you communicate with the API. This part lays all requests here.
- **/create** - POST - Creates a note.
- **/edit** - POST - Edits a note. Basically you can edit notename and/or notedata and/or notetype. Same structure as before.
- **/delete** - POST - Deletes a note (and permamently deletes the last note it called twice). Requires a UUID of the note, there can only be one recoverable/perm delatable note with UUID 0.
- **/getnotes/*n*** - GET - Returns all the notes with 10 notes in each page ({n} = page number).
- **/star** - POST - Stars (internally Favorites) a note. Requires note's UUID.
- **/lastdeleted** - GET - Returns the last deleted note.
- **/lastcreated** - GET - Returns the last created note.
- **/lastused** - GET - Returns the last used.
- **/search** - POST - Returns notes with notename partically/fully match the search_query.
- **/copy** - POST - Duplicates a note with a new UUID.
- **/recover** - GET - Recovers the last deleted note.
- **/help** - GET - Help Page
- **/** - GET - Hello World!

## JSON for POST requests
JSON is the only way to request something specific, be it search or deletion. Here lays every data class and it's use.
- **noteid**: UUID of any given note. Used when doing /edit./star,/delete, and /copy
- **noteowner**: Name of the user posting the note (currently whatever you want)
- **notename**: Name of the note itself
- **notedata**: Data of the note
- **notetype**: Data type of the note (txt, md, json, or even png technically)
- **notecreatedate**: Creation date of the note/Deletion date of the note (in case noteid=0)/Recovery of the note
- **noteeditdate**: Edit date of the note (notecreatedate by default; resets after /recovery)

- **search_query**: Exclusive to /search. A string used to match notename

## POST templates for each API POST request
This is the section with templates for each POST request. Please follow this template. NOTE: "Optional" means not required when sending the request.
- /create: {"noteowner":"","notename":"","notedata":"","notetype":""}
- /edit: {"noteid":"","notename":"Optional",""notedata:"Optional","notetype":"Optional"}
- /star: {"noteid":""}
- /delete: {"noteid":""}
- /copy: {"noteid":""}
- /search: {"search_query":""}

# Database config/structure
To better understand what lies under the hood, here are the data classes used in the postgresql database.
- noteid = uuid DEFAULT gen_random_uuid()
- notename = VARCHAR(255)
- noteowner = VARCHAR(32)
- notedata = TEXT NOT NULL
- notetype = VARCHAR(8)
- favorite = BOOLEAN
- notecreatedate = TIMESTAMP
- no-teeditdate = TIMESTAMP

# 

## Directory Highearchy:
- /API -- has the requests, dataclasses, and testing.
- /Database -- has managing of the database, and bridging SQL and Python.
- /GUI -- has the future GTK4 GUI. Please help me i need help
