import mysql.connector

mydb = mysql.connector.connect(
  host="148.205.37.150",
  user="team1",
  passwd="team1nti#"
)
print(mydb)
cursor=mydb.cursor()
"""
query= ("SELECT date, time, kwh FROM meterlogs.logs")
cursor.execute(query)
for( time, date, kwh) in cursor:
  print("{}, {}, {}".format(date, time, kwh) )
"""
query= ("SELECT date, time, kwh FROM meterlogs.logs WHERE time >%s AND time <%s AND date = %s")
start_time= '21:00:00'
end_time='22:00:00'
miguel_date= '2019-02-26'
cursor.execute(query, (start_time,end_time,miguel_date))
for( time, date, kwh) in cursor:
  print("{}, {}, {}".format(date, time, kwh) )


cursor.close()
mydb.close()



