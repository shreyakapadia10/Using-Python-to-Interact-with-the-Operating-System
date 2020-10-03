# readlines() method reads whole file at once and we can use it like below

file = open("demo_file.txt")
lines = file.readlines()
file.close()
lines.sort()
print(lines)
