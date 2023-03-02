import mysql.connector as connector

mysql_connect = connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="root",
    database="w3schools"
)

with mysql_connect.cursor() as cursor:
    cursor.execute("SELECT * FROM categories")

    fetchall = cursor.fetchall()

    columns = [col[0] for col in cursor.description]

    for row in fetchall:
        print(dict(zip(columns, row)))

print(mysql_connect.is_connected())
