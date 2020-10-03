import csv

f = open('csv_file.csv')
read_csv = csv.reader(f)

for row in read_csv:
    name, phone, field = row
    print("Name: {}, Phone: {}, Field: {}".format(name, phone, field))

f.close();
