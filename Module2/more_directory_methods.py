import os

# Listing all files and directories in Current Working Directory
print("Listing all files/directories of new_dir: ")
print(os.listdir("new_dir"))
print()
# Checking whether the list provided by os.listdir is file or directory
# Use of os.path.join --> it joins the directory name with another name of file/directory using forward slash for Linux and MacOS and by backward slash for Windows
# Use of os.path.isdir() --> Checks whether the name supplied is a file or a directory

lists = os.listdir("new_dir")
dir_name = "new_dir"

for name in lists:
    fullName = os.path.join(dir_name, name)

    if os.path.isdir(fullName):
        print("{} is a Directory.".format(fullName))
    else:
        print("{} is a File.".format(fullName))
