import openpyxl
import xlrd
import mysql.connector

db_config = {
    "host": "localhost:3306",
    "user": "root",
    "password": "root",
    "database": "test_db",
}

# connection = mysql.connector.connect(**db_config)
# Get the cursor, which is used to traverse the database, line by line
# cursor = connection.cursor()

workbook = openpyxl.load_workbook(r'DATA_mau-2.xlsx')
sheet_name = workbook['Template Phatsinh']
all_rows = sheet_name.iter_rows(min_row=2, values_only=True)

for (i, row) in enumerate(all_rows, start=2):
    if row:
        print(i, row)

# Create the INSERT INTO sql query
# query = "INSERT INTO orders (product, customer_type, rep, date, actual, expected, open_opportunities, closed_opportunities, city, state, zip, population, region) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

# Create a For loop to iterate through each row in the XLS file, starting at row 2 to skip the headers
# for r in range(1, sheet.nrows):
#     print(sheet.cell(r, ).value)
#     print(sheet.cell(r, 1).value)
    # product = sheet.cell(r, ).value
    # customer = sheet.cell(r, 1).value
    # rep = sheet.cell(r, 2).value
    # date = sheet.cell(r, 3).value
    # actual = sheet.cell(r, 4).value
    # expected = sheet.cell(r, 5).value
    # open = sheet.cell(r, 6).value
    # closed = sheet.cell(r, 7).value
    # city = sheet.cell(r, 8).value
    # state = sheet.cell(r, 9).value
    # zip = sheet.cell(r, 10).value
    # pop = sheet.cell(r, 11).value
    # region = sheet.cell(r, 12).value

    # values = (product, customer, rep, date, actual, expected, open, closed, city, state, zip, pop, region)
    # cursor.execute(query, values)

# cursor.close()
# connection.commit()
# connection.close()
