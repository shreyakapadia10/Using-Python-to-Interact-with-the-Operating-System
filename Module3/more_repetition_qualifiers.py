# We can use a '{}' to specify a perticular range
import re
print("Using Search: ")
print(re.search(r'[a-zA-Z]{5}', "The ghost is scary"))
print(re.search(r'[a-zA-Z]{5}', "A scary ghost appeared"))

print("Using findall:")
print(re.findall(r'[a-zA-Z]{5}', "A scary ghost appeared"))

print("Using \\b: ")
print(re.findall(r'\b[a-zA-Z]{5}\b', "A scary ghost appeared"))

print("Two numbers in range: ")
print(re.findall(r'\w{5,10}', "I really like straberries"))

print("From minimum range of 5: ")
print(re.findall(r'\w{5,}', "I really like straberries"))

print("From range of 0 to some number: ")
print(re.search(r's\w{,20}', "I really like straberries"))
