#!/usr/bin/env python3
import re
import operator
import csv

# Initializing dictionaries
error = {}
per_user = {}

with open('syslog.log') as file:
    for line in file:
        # Line Strip to remove any additional spaces
        line=line.strip()

        # Regular Expression to match given condition to check whether the line contains ERROR or INFO
        info_error = re.search(r"(INFO|ERROR) ([\w ']*)", line).group(1)

        # Regular Expression to match given condition to check whether the line contains valid username
        user = re.search(r"\(([\w\.]*)\)$", line).group(1)

        # If info_error is None i.e. it doesn't match any pattern
        if info_error is None:
            continue

        # Add username to dictionary per_user if it is not there
        if user not in per_user:
            user_count = {'INFO': 0, 'ERROR': 0}
            per_user[user] = user_count

        # Else increment the value of INFO or ERROR by 1
        per_user[user][info_error] += 1

        # IF info_error is ERROR add it to error dictionary
        if info_error == 'ERROR':
            # Get the Error message
            err = re.search(r"ERROR ([\w ']*) ", line).group(1)
            error[err] = error.get(err, 0) + 1

file.close()

errors = []
users = []

# Sorting by maximum number of errors and appending Error and it's count to list errors
for key, value in sorted(error.items(), key=operator.itemgetter(1), reverse=True):
    errors.append([key, value])

# Sorting by username and appending username, info counts and error counts to list users
for key in sorted(per_user.keys()):
    users.append([key, per_user[key]['INFO'], per_user[key]['ERROR']])

# Adding Titles
users.insert(0, ['Username', 'INFO', 'ERROR'])
errors.insert(0, ['ERROR', 'Count'])

# Writing errors to error_message.csv
with open('error_message.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(errors)

# Writing user info/error to user_statistics.csv
with open('user_statistics.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(users)

print("Report Generated Successfully!")
