import csv

data = [{'name': "Shreya Kapadia", "department": "CP", "phone": 8849166573},
        {'name': "Roshani Jawale", "department": "CP", "phone": 9874563210},
        {'name': "Nency Tailor", "department": "Architecture", "phone": 9632587410}]

keys = ["name", "department", "phone"]

with open("dict_data.csv", "w") as file:
    writer = csv.DictWriter(file, fieldnames=keys)
    writer.writeheader()
    writer.writerows(data)
