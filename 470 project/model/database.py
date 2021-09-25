import mysql.connector

mydb = mysql.connector.connect(host='localhost',
                               user='root',
                               password='',
                               database='atm users')
if mydb.is_connected():
    print("connected")
mydb.close()

mycursor = mydb.cursor()

mycursor.execute()

