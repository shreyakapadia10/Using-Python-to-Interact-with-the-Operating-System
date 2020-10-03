import re

print("To print string that contain python either uppercase or lowercase 'p': ")
print(re.search(r'[Pp]ython', 'Python'))

print("To search for a string preceeded by any letter: ")
print(re.search(r'[a-z]way', 'The end of the highway'))

print('What if we put " way" in matching string?')
print(re.search(r'[a-z]way', 'This is wrong way'))

print("Defining range for upper/lower letters and digits: ")
print(re.search(r'cloud[a-zA-Z0-9]',"cloudy"))

print(re.search(r'cloud[a-zA-Z0-9]',"cloud9"))

print("To match characters that aren't in given pattern(using circumflex inside square brackets[^]): ")
print(re.search(r'[^a-zA-Z0-9]', "This sentence will match to space."))
print(re.search(r'[^a-zA-Z0-9 ]', "This sentence will match to dot."))

print("To match either one or other expression: ")
print(re.search(r'cat|dog', "I like cats."))
print(re.search(r'cat|dog', "I don't like dogs."))
print(re.search(r'cat|dog', "I like both dogs and cats."))

print("To match both of the expression use findall: ")
print(re.findall(r'cat|dog', "I like both cats and dogs."))
