import mysql.connector 

mydb=mysql.connector.connect{
host="localhost",
user="root",
passwd="1234",
database="testdb"
}
mycursor=mydb.cursor()
mycursor.execute("CREATE TABLE students(name varchar(255),age integer(10))")