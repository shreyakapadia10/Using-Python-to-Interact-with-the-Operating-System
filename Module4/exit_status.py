import os
import sys

print("Check Exit status using echo %ErrorLevel% for windows")
print("Check Exit status using $? for Linux")
filename = sys.argv[1]

if not os.path.exists(filename):
    with open(filename, 'w') as file:
        file.write("This is newly created file")
else:
    print("File {} already exists".format(filename))
    sys.exit(1)
