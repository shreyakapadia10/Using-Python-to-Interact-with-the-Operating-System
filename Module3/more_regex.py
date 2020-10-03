import re

print("To check for the countries that starts and ends with 'a' (not correct way): ")
print(re.search(r'A.*a', 'Argentina'))
print(re.search(r'A.*a', 'Azerbaijan'))

print("To check for the countries that starts and ends with 'a' (correct way): ")
print("Using circumflex to start a name with 'A' and $ to end the name with 'a'")
print(re.search(r'^A.*a$', 'Azerbaijan'))
print(re.search(r'^A.*a$', 'Argentina'))
