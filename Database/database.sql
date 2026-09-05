-- create
CREATE TABLE NOTES (
  noteid UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  notename VARCHAR(255),
  noteowner VARCHAR(32),
  notedata TEXT NOT NULL,
  notetype VARCHAR(8),
  favorite BOOLEAN,
  notecreatedate TIMESTAMP,
  noteeditdate TIMESTAMP
);

-- insert
INSERT INTO NOTES (notename,noteowner,notedata,notetype,favorite,notecreatedate,noteeditdate) VALUES ('TestNote','root','This is *a test*', 'md',true,CURRENT_TIMESTAMP,CURRENT_TIMESTAMP);
INSERT INTO NOTES (notename,noteowner,notedata,notetype,favorite,notecreatedate,noteeditdate) VALUES ('TestNote2','user1','This is *another test*', 'md',false,CURRENT_TIMESTAMP,CURRENT_TIMESTAMP);
INSERT INTO NOTES (notename,noteowner,notedata,notetype,favorite,notecreatedate,noteeditdate) VALUES ('TxtNote','user1','This is a txt text', 'txt',false,CURRENT_TIMESTAMP,CURRENT_TIMESTAMP);
INSERT INTO NOTES (notename,noteowner,notedata,notetype,favorite,notecreatedate,noteeditdate) VALUES ('FavoriteNote','user1','This is a starred test', 'md',true,CURRENT_TIMESTAMP,CURRENT_TIMESTAMP);
INSERT INTO NOTES (notename,noteowner,notedata,notetype,favorite,notecreatedate,noteeditdate) VALUES ('TestNote55','user2','This is *another test* from **another** user', 'md',false,CURRENT_TIMESTAMP,CURRENT_TIMESTAMP);




-- fetch 
SELECT * FROM NOTES;
