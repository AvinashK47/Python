import mysql.connector
mydb = mysql.connector.connect(
    host = 'amnesia',
    user = 'avinash',
    passwd= '1234'
)

cursor = mydb.cursor()

cmd1 = "CREATE DATABASE MyDatabase"

cursor.execute(cmd1)