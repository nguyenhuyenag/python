import mysql.connector

datasource = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="sakila"
)

print(datasource)

cursor = datasource.cursor()

cursor.execute("SELECT * FROM city")

result = cursor.fetchall()

# for x in result:
#     print(x)

size = len(result)

for i in range(0, size):
    print(result[i][0])

