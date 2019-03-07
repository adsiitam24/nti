import datetime
import mysql.connector
import random

ids = []
mydb = mysql.connector.connect(
  host="148.205.37.150",
  user="team1",
  passwd="team1nti#"
)
cursor=mydb.cursor()
loc = 'EFRA2'
n = 3
queryMax = ("SELECT * from taglogs.tagmessages WHERE tag='EB01' ORDER BY tagmessages.id DESC LIMIT " + str(n))
cursor.execute(queryMax)
for(id) in cursor:
  ids.append(id[0])
print(ids)

for i in ids:
  query = ("UPDATE taglogs.tagmessages SET location='" + loc + "' WHERE id=" + str(i))
  cursor.execute(query)
  mydb.commit()
queryMax = ("SELECT * from taglogs.tagmessages WHERE tag='EB01' ORDER BY tagmessages.id DESC LIMIT " + str(n))
cursor.execute(queryMax)
for( id) in cursor:
  print("{}".format(id))
cursor.close()
mydb.close()



