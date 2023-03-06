from getpass import getpass
from mysql_db.connector import connect, Error

try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
    ) as connection:
        print(connection)
except Error as e:
    print(e)


connection_properties = {
    'host': 'localhost',
    'port': 3306,
    'user': "root",
    'password': "root",
    'database': 'w3schools'
}

cnx = mysql.connector.connect(**connection_properties)
cnx.close()

