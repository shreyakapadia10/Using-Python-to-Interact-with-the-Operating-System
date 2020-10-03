# \w = for alphanumeric characters i.e. letters, digits, underscore
# \d = for digits
# \s = for spaces, new line, tabs
# \b = for word boundries

import re

print("What if we want to print something starting with '.' ?")
print(re.search(r'.com', 'Welcome'))

print("Thus use escaping characters '\\'")
print(re.search(r'\.com', 'google.com'))

print("Using \w: ")
print(re.search(r'\w*', 'This is a sentence'))
print(re.search(r'\w*', 'This_is_a_sentence'))
