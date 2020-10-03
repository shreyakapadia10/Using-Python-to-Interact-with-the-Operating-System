# Use of Directory Methods
import os

print("Printing Current Working Directory: ")
print(os.getcwd())

print("Use of mkdir method: ")
os.mkdir("new_dir")

print("Changing Working Directory: ")
os.chdir("new_dir")

print("Again Printing Current Working Directory: ")
print(os.getcwd())

os.mkdir("new_dir2")

print("Removing a Directory(We can't remove directories having files in it): ")
os.rmdir("new_dir2")
