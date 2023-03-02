import mysql.connector as connector

mysql_connect = connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="root",
    database="w3schools"
)

cursor = mysql_connect.cursor()
cursor.execute("SELECT * FROM categories")
# [('categories',), ('customers',), ('employees',), ('order_details',), ('orders',), ('products',), ('shippers',), ('suppliers',)]

fetchall = cursor.fetchall()

columns = [col[0] for col in cursor.description]

for row in fetchall:
    print(dict(zip(columns, row)))

