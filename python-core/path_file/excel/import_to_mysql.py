import openpyxl
import mysql.connector
from datetime import datetime


def to_mysql_datetime(str_date, pattern='%d/%m/%Y'):
    str_date = datetime.strptime(str_date, pattern)
    return str_date.strftime('%Y-%m-%d')


db_config = {
    "host": "localhost",
    "port": "3306",
    "user": "root",
    "password": "root",
    "database": "test_db",
}

# connection = mysql.connector.connect(**db_config)

# if connection.is_connected():
#     print("Kết nối đến MySQL thành công")
# else:
#     print("Kết nối đến MySQL thất bại")

# cursor = connection.cursor()
# print(cursor)


workbook = openpyxl.load_workbook(r'DATA_mau-2.xlsx')
sheet_name = workbook['Template CDCS']
all_rows = sheet_name.iter_rows(min_row=2, values_only=True)

sql_query = "INSERT INTO tra_soat (hoten, so_bhxh, ngaysinh, tu_thangnam) VALUES (%s, %s, %s, %s)"

try:
    with mysql.connector.connect(**db_config) as connection:
        with connection.cursor() as cursor:
            for (i, row) in enumerate(all_rows, start=2):
                print(row[14])
                # hoten       = row[1]
                # so_bhxh     = row[2]
                # ngaysinh    = to_mysql_datetime(row[3])
                # tu_thangnam = to_mysql_datetime(row[4], '%m/%Y')

                # values = (hoten, so_bhxh, ngaysinh, tu_thangnam)
                # print(values)

                # cursor.execute(sql_query, values)

        # Commit the transaction (changes) to the database
        connection.commit()
except mysql.connector.Error as err:
    print(f"Error: {err}")
