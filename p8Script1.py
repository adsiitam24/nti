import datetime
import mysql.connector
import random

mydb = mysql.connector.connect(
  host="148.205.37.150",
  user="team1",
  passwd="team1nti#"
)
print(mydb)
cursor=mydb.cursor()
now = datetime.datetime.now()
seq = 0
n = 3
hora = '12:35:'
seg = 0
segStr = ''
id = 1100
for i in range(n):
  if seg < 10:
    segStr = '0'+ str(seg)
  else:
    segStr = str(seg)
  query= ("INSERT INTO taglogs.tagmessages VALUES("+str(id)+",'EB01','0002'," + str(seq) +",'" + str(now.year)+"-"+str(now.month)+"-"+str(now.day)+ "','" + hora+segStr+ "'," + str(random.randint(-100,-50)) +",'null');")
  print(query)
  cursor.execute(query)
  mydb.commit()
  id += 1
  query= ("INSERT INTO taglogs.tagmessages VALUES("+str(id)+",'EB01','0005'," + str(seq) +",'" + str(now.year)+"-"+str(now.month)+"-"+str(now.day)+"','" + hora+segStr + "'," + str(random.randint(-100,-50)) +",'null');")
  print(query)
  cursor.execute(query)
  mydb.commit()
  id += 1
  query= ("INSERT INTO taglogs.tagmessages VALUES("+str(id)+",'EB01','0002'," + str(seq) +",'" + str(now.year)+"-"+str(now.month)+"-" +str(now.day)+"','" + hora+segStr+ "'," + str(random.randint(-100,-50)) +",'null');")
  print(query)
  cursor.execute(query)
  mydb.commit()
  seg += 1
  if seg == 60:
    seg = 0
  seq += 1
  if seq == 256:
    seq = 0
  id += 1
cursor.close()
mydb.close()



