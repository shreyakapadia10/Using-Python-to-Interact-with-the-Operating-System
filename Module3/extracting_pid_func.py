import re

def extracting_pid(log_line):
    regex = r'\[(\d+)\]'
    result = re.search(regex, log_line)

    if result is None:
        return "No match found for: {}".format(log_line)
    return "{}".format(result[1])

log = "99 elephants in [cage]"
print(extracting_pid(log))

log = "This is an error msg [12345]: ERROR with code in square brackets"
print(extracting_pid(log))
