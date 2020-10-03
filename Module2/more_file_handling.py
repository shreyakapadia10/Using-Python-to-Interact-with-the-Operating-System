import os

# To get size of file
print("File size using os.path.getsize(in bytes): {}".format(os.path.getsize('demo_file.txt')))

# To get last modified time of file will return time from 1st january, 1970
print("Last modified time using os.path.getmtime: {}".format(os.path.getmtime('demo_file.txt')))

# To get more readable time
import datetime

timestamp = os.path.getmtime('demo_file.txt')
print("Last modified time in human readable form using datetime.datetime.fromtimestamp: {}".format(datetime.datetime.fromtimestamp(timestamp)))

# To get absolute path of a file
print("Printing absolute path of file using os.path.abspath: {}".format(os.path.abspath('demo_file.txt')))
