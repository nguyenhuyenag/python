# import mysql.connector as mysql_connector
#
# mydb = mysql_connector.connect(
#     host="localhost",
#     user="root",
#     password="root",
#     database="w3schools"
# )
#
# cursor = mydb.cursor()
# cursor.execute("SELECT * FROM categories")
# # [('categories',), ('customers',), ('employees',), ('order_details',), ('orders',), ('products',), ('shippers',), ('suppliers',)]
# fetchall = cursor.fetchall()
# columns = [col[0] for col in cursor.description]
# for row in fetchall:
#     print(dict(zip(columns, row)))
#
