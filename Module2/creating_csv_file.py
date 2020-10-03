import csv

data = [["Shreya Kapadia", 8849166573, "CP"],["Roshani", 9874563210, "CP"],["Nency",1236547890, "Arch."]]

# writerow to write each row at a time
# writerows to write all data at a time

with open('data_csv.csv','w') as data_csv:
    write = csv.writer(data_csv)
    write.writerows(data)
