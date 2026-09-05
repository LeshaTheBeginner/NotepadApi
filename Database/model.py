import sqlalchemy  
import datetime as dt  
engine = sqlalchemy.create_engine('postgresql://postgres@127.0.0.1:5432/notesdb')  #psql "postgresql://username:password@hostname:5432/dbname"
connection = engine.connect()  
metadata = sqlalchemy.MetaData()
  
noteTable = sqlalchemy.Table('notes', metadata,  
	           sqlalchemy.Column('noteid', sqlalchemy.Uuid()),  
	           sqlalchemy.Column('notename', sqlalchemy.String(255), nullable=False,default='Unnamed'),
	           sqlalchemy.Column('noteowner', sqlalchemy.String(32), default='user1'),  
	           sqlalchemy.Column('notedata', sqlalchemy.String(), default='Nothing to read!'),
               sqlalchemy.Column('notetype', sqlalchemy.String(8), default='md'),
               sqlalchemy.Column('favorite', sqlalchemy.Boolean(), default=False),
               sqlalchemy.Column('notecreatedate', sqlalchemy.TIMESTAMP(), default=dt.datetime.now()), #dt.datetime(1979,1,1,13,13,13,0)
               sqlalchemy.Column('noteeditdate', sqlalchemy.TIMESTAMP(), default=dt.datetime.now())
	  )  
  
metadata.create_all(engine)