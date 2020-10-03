import re
pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"

print(re.search(pattern, 'This is not valid variable name'))
print(re.search(pattern, '_this_is_valid_variable_name'))
print(re.search(pattern, 'this_also9'))
print(re.search(pattern, '0not_this'))
