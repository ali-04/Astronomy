import mysql.connector

SQL = mysql.connector.connect(user='root' , password='41148' , host='localhost' , database='tst')

cursor = SQL.cursor()

result = cursor.fetchall()

result.sort(key=lambda x : x[2] )

# result.reverse()

for later in result :
    print(later)