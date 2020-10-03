with open("demo_file.txt") as file:
    for line in file:
        print(line.upper())

with open("demo_file.txt") as file1:
    for line in file1:
        print(line.strip().upper())
