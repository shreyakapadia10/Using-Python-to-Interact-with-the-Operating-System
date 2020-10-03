# 'r'= open for reading (default)
# 'w' = open for writing, truncating the file first
# 'x'= open for exclusive creation, failing if the file already exists
# 'a' = open for writing, appending to the end of the file if it exists
# 'b' = binary mode
# 't' = text mode (default)
# '+' = open for updating (reading and writing)
# Writing into file - If file doesn't exist it will create one, but if exist, it'will be deleted as soon as file opens

with open("new_file.txt", "w") as file:
    file.write("Hello there! I'm writing into this file using Python!!")
