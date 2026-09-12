import sqlalchemy
from pprint import pprint  
from model import engine,noteTable,metadata


connection = engine.connect()
  
# query = sqlalchemy.select(noteTable)
# q + value = query value
qfavorite = sqlalchemy.select(noteTable).where(noteTable.columns.favorite == True)
qnewest = sqlalchemy.select(noteTable).order_by(noteTable.columns.notecreatedate)
#qcreatenew = sqlalchemy.insert(noteTable).values(noteowner='test.py',notedata='Test for test.py inserting with code',favorite=True,)
qselect = sqlalchemy.select(noteTable).where(noteTable.columns.noteid == "799f6e39-b28e-4c57-a66f-7d20ef705a6c")

# result_proxy = connection.execute(qfavorite)

result_proxy = connection.execute(qnewest)
result_set = result_proxy.fetchall()

pprint(result_set)

# connection.commit()