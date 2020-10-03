import re

result = re.search(r'^(\w*), (\w*)$', "Kapadia, Shreya")
print(result)
print(result.groups())
print("Prints whole matched String result[0]: ")
print(result[0])
print("Prints only String result[1]: ")
print(result[1])
print("Prints only String result[2]: ")
print(result[2])
#"^([\w \.-]*), ([\w \.-]*)$
print("My name is: {} {}".format(result[2], result[1]))
