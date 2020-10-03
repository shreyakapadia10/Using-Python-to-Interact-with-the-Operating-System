import re
import sys

logfile = sys.argv[1]
usernames = {}
with open(logfile) as file:
    for line in file:
        if "CRON" not in line:
            continue
        pattern = r"\((\w+)\)$"
        result = re.search(pattern, line.strip())

        if result is None:
            continue

        name = result[1]
        usernames[name] = usernames.get(name, 0) + 1
print(usernames)
