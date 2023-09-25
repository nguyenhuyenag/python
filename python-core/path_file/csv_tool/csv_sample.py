import csv
import pandas as pd

filename = 'employees.csv'


def write_normal():
    with open(filename, newline='', mode='w') as stream:
        employee_writer = csv.writer(stream, delimiter=',')
        employee_writer.writerow(['James', '001', 22, 'sales', True])
        employee_writer.writerow(['John', '002', 28, 'engineering', False])
        employee_writer.writerow(['Jessica', '003', 25, 'engineering', True])
        employee_writer.writerow(['Monica', '004', 29, 'accounting', False])


def write_dict():
    with open('employees_dict.csv', 'w') as csv_file:
        header = ['name', 'id', 'age', 'department', 'likes_pizza']
        data = [
            ['Jack', '008', '20', 'sales', True],
            ['Jess', '006', '32', 'accounting', True],
            ['Wendy', '009', '22', 'accounting', True],
            ['Lisa', '007', '21', 'engineering', False],
        ]
        writer = csv.DictWriter(csv_file, fieldnames=header, lineterminator='\n')
        writer.writeheader()
        for row in data:
            pairs = zip(header, row)
            writer.writerow(dict(pairs))


def read_normal():
    with open(filename) as csv_file:
        reader = csv.reader(csv_file)
        # reader = csv.reader(csv_file, delimiter=',', quotechar='"')
        for row in reader:
            print(row)


def add_header_to_csv():
    df = pd.read_csv(filename, header=None)
    header = ['name', 'id', 'age', 'department', 'likes_pizza']
    df.to_csv(filename, header=header, index=False)


# write_normal()
# write_dict()
read_normal()
# add_header_to_csv()
