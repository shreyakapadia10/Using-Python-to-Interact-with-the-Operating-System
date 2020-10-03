import re

log = "This is an error msg [12345]: ERROR with code in square brackets"
regex = r'\[(\d+)\]'
result = re.search(regex, log)
print(result[1])

result = re.search(regex, "This is another log [69854220]")
print(result[1])

print("The following line will generate error: ")
result = re.search(regex, "99 elephants in [cage]")
print(result[1])
