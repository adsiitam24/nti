import datetime
import mysql.connector

mydb = mysql.connector.connect(
  host="148.205.37.150",
  user="team1",
  passwd="team1nti#"
)
print(mydb)
cursor=mydb.cursor()
now = datetime.datetime.now()
"""
query= ("INSERT INTO tagmessages VALUES('EB01', '0002'," + int(seq) +"," + now.year+"-"+now.month+"-"+now.day + "," + now.hour+":"+now.minute+":"+now.second + "," + randon.random(-100,-50) +")")
cursor.execute(query)

"""
seq = 0
n = 1
hora = '12:05:'
seg = 0
for i in range(n)
	seq += 1
	query= ("INSERT INTO tagmessages VALUES('EB01', '0002'," + int(seq) +"," + now.year+"-"+now.month+"-"+now.day + "," + hora+str(seg)+ "," + randon.random(-100,-50) +")")
	cursor.execute(query)
	seq += 1
	query= ("INSERT INTO tagmessages VALUES('EB01', '0005'," + int(seq) +"," + now.year+"-"+now.month+"-"+now.day + "," + hora+str(seg) + "," + randon.random(-100,-50) +")")
	cursor.execute(query)
	seq += 1
	query= ("INSERT INTO tagmessages VALUES('EB01', '0002'," + int(seq) +"," + now.year+"-"+now.month+"-"+now.day + "," + hora+str(seg) "," + randon.random(-100,-50) +")")
	cursor.execute(query)
	seg += 3

cursor.close()
mydb.close()



