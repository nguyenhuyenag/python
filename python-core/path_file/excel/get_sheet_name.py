import openpyxl


wb = openpyxl.load_workbook('DATA_mau-2.xlsx')

def method_1():
    sheet_names = wb.sheetnames
    for sheet_name in sheet_names:
        print(sheet_name)

# Get the second sheet by index (index 1)
second_sheet = wb.worksheets[0].title
print('By index:', second_sheet)

method_1()
