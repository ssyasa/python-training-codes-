import mysql.connector

# Create a connection to the MySQL server
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="ssni6161"  # Replace with your MySQL password
)

# Create a cursor object to interact with the database
mycursor = mydb.cursor()

# Create a new database (if it doesn't exist)
mycursor.execute("CREATE DATABASE IF NOT EXISTS testdb")

# Use the newly created database
mycursor.execute("USE testdb")

# Create a table to store student data
mycursor.execute("CREATE TABLE IF NOT EXISTS students (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)")

# Define the SQL query template for inserting data into the table
sqlFormula = "INSERT INTO students (name, age) VALUES (%s, %s)"

# Define a list of student data to insert into the database
students = [
    ("Alice", 20),
    ("Bob", 22),
    ("Charlie", 21),
    ("David", 23)
]

# Use executemany to insert multiple records into the table
mycursor.executemany(sqlFormula, students)

# Commit the changes to the database
mydb.commit()

# Close the cursor and the database connection
mycursor.close()
mydb.close()
