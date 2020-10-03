import re

# Similar to split in string
print("Using split: ")
print("Without .?! : ")
print(re.split(r'[.?!]', 'This is one sentence. And this one too? and yet last question!'))

print("With .?! : ")
print(re.split(r'([.?!])', 'This is one sentence. And this one too? and yet last question!'))

# Similar to replace
print("Using sub:")
print(re.sub(r'[\w.%+-]+@[\w.-]+', '[REDACTED]', 'This email is forgeemail78@forge.com.in'))

print("Using sub for names: ")
print(re.sub(r'([\w \.-]*), ([\w \.-]*)', r'\2 \1', 'Kapadia, Shreya D.'))
