import re

# '.*' tries to include 0 or as many characters as possible
print("Using .* :")
print(re.search(r'Pr.*m', 'Program'))
print(re.search(r'Py.*n', "Python Programming"))

print("Using * : ")
print(re.search(r'Py[a-z]*n', 'Python Programming'))
print(re.search(r'Py[a-z]*n', 'Pyn'))

# '+' matches 1 or more occurences of characters that comes before it
print("Using '+' : ")
print(re.search(r'o+l+', 'wolf'))
print(re.search(r'o+l+', 'coolie'))

# '?' matches 0 or more occurences of characters that comes before it [means optional]
print("Using ? :")
print(re.search(r'p?each', 'To each their own'))
print(re.search(r'p?each', 'I like peaches'))
