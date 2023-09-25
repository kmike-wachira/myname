import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pythontest"
)

cursor = conn.cursor()


def createTable():
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS wokers(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")
    conn.commit()
    print("Table Created")


def showTables():
    cursor.execute("SHOW TABLES")
    for x in cursor:
        print(x)


def insert_users():
    username = input("enter your name \n")
    user = (username,)
    print(user)
    sql = "INSERT INTO wokers(name) VALUES(%s)" 
    cursor.execute(sql, user)
    conn.commit()
    print("Data inserted")


def readAll():
    cursor.execute("SELECT * FROM wokers")
    for x in cursor:
        print(x)


# readAll()
name, age, marks = input("Enter your Name, Age, Percentage separated by space ").split()

print(name,age,marks)

