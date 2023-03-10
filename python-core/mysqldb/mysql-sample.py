from contextlib import closing
import mysql.connector as connector
from mysql.connector import FieldType
from dbsettings import connection_properties


def select():
    with closing(connector.connect(**connection_properties)) as mysql_connect:
        cursor = mysql_connect.cursor()
        cursor.execute("SELECT * FROM shippers")

        # cursor.fetchone()
        # cursor.fetchmany(size=2)
        fetch_all = cursor.fetchall()

        # The number of rows for the SELECT stataments
        print("Row:", cursor.rowcount)

        # Get query
        # print(cursor.statement)

        # print(cursor.fetchwarnings())

        columns = cursor.column_names
        # columns = [col[0] for col in cursor.description]

        for row in fetch_all:
            print(dict(zip(columns, row)))


def insert():
    with closing(connector.connect(**connection_properties)) as mysql_connect:
        cursor = mysql_connect.cursor()
        data = [
            ('Rafael Nadal (2)', '(503) 555-9832'),
            ('Rafael Nadal (3)', '(503) 555-9833'),
            ('Rafael Nadal (4)', '(503) 555-9834'),
        ]
        sql = "INSERT INTO shippers (ShipperName, Phone) VALUES (%s, %s)"
        cursor.executemany(sql, data)

        # The AUTO_INCREMENT value before insert
        incr_id = cursor.lastrowid
        print("incr_id:", incr_id)

        mysql_connect.commit()
        print("%d record inserted" % cursor.rowcount)


"""
    (
        column_name,
        type,
        None,
        None,
        None,
        None,
        null_ok,
        column_flags
    )
"""

def description():
    with closing(connector.connect(**connection_properties)) as mysql_connect:
        cursor = mysql_connect.cursor()
        cursor.execute("SELECT * FROM shippers")

        for i in range(len(cursor.description)):
            print("Column {}:".format(i + 1))
            desc = cursor.description[i]
            print("\tcolumn_name = {}".format(desc[0]))
            print("\ttype = {} ({})".format(desc[1], FieldType.get_info(desc[1])))
            print("\tnull_ok = {}".format(desc[6]))
            print("\tcolumn_flags = {}".format(desc[7]))


# insert()
select()
# description()
# mysql_connect.close()
# print(mysql_connect.is_connected())
