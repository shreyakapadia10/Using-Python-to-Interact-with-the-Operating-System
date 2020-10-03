import os

# Removing file
os.remove("file_meant_to_be_deleted.txt")

# Renamin file
os.rename("file1.txt", "final_flie.txt")

# Checking if file does exist? It can be checked by submodule of OS known as path
result = os.path.exists("file_meant_to_be_deleted.txt")
print(result)

result = os.path.exists("final_flie.txt")
print(result)
