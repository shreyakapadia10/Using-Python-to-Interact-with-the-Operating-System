file = open("demo_file.txt")

# reading 1st line
print(file.readline())
# reading 2nd line
print(file.readline())

# reading from 3rd line to eof
print(file.read())

file.close()
