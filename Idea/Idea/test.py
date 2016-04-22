import mysql.connector
conn = mysql.connector.connect(host='127.0.0.1', database='Test', user='root', password='gena')
mycursor = conn.cursor()
mycursor.execute('SELECT * FROM Test.Users')
result = mycursor.fetchall()
for (Id,Name,Email) in result:
    print (Id)
    print (Name + '/' + Email)
    print (Email)
conn.close

import pymysql
pymysql.install_as_MySQLdb()
conn1 = pymysql.connect(host='127.0.0.1', database='Test', user='root', password='gena')
mycursor = conn1.cursor()
mycursor.execute('SELECT * FROM Test.Users')
result = mycursor.fetchall()
for (Id,Name,Email) in result:
    print (Id)
    print (Name + '/' + Email)
    print (Email)
conn1.close