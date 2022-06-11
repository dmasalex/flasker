import mysql.connector

mydb = mysql.connector.connect(
	host='localhost',
	user='alex',
	passwd='123QWE'
	)

my_cursor = mydb.cursor()

#my_cursor.execute("CREATE DATABASE flask_db") ВЕРНУТЬ ПРИ СОЗДАНИИ БД
my_cursor.execute("SHOW DATABASES")

for db in my_cursor:
	print(db)