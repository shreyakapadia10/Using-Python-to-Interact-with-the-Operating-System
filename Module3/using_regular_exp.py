import re

log = "This is the log file data error: [123456] having such errors"
regex = r"\[(\d+)]"
result = re.search(regex, log)
print(result[1])
