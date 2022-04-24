import mysql.connector

myDB = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
    # database="" to work with a database
)

mycursor = myDB.cursor()
mycursor.execute(
    "SHOW DATABASES")  # Write sql statements/queries here like SHOW DATABASES, SHOW TABLES,CREATE TABLE NAMETBLE
# CREATE DATABASE DBNAME

# mycoursor = myDB.cursor("SELECT * from tablename")
# myresult = mycursor.fetchall() print myresult in loop

for x in mycursor:
    print(x)
