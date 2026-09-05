import sqlalchemy
from pprint import pprint  
from model import engine,noteTable,metadata
  

connection = engine.connect()  
  
# query = sqlalchemy.select(noteTable)
# q + value = query value
qfavorite = sqlalchemy.select(noteTable).where(noteTable.columns.favorite == True)
qnewest = sqlalchemy.select(noteTable).order_by(noteTable.columns.notecreatedate)
qcreatenew = sqlalchemy.insert(noteTable).values(noteowner='test.py',notedata='Test for test.py inserting with code',favorite=True,)

result_proxy = connection.execute(qcreatenew)

result_proxy = connection.execute(qnewest)
result_set = result_proxy.fetchall()

pprint(result_set)

connection.commit()