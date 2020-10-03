import csv

with open("another_csv.csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print("{} studies in {} department".format(row["name"], row["department"]))
