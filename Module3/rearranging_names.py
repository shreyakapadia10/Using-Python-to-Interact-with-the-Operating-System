import re
def rearranging_names(name):
    pattern = r'^(\w*), (\w*)$'
    result = re.search(pattern, name)
    if result is None:
        return "{}".format(name)
    return "{} {}".format(result[2], result[1])

print(rearranging_names('Kapadia, Shreya'))
print(rearranging_names('Kapadia, Shivani'))
print(rearranging_names('Kapadia, Harshil D.'))

# For middle name this_also
print()
print("For middle names: ")
def rearranging_names_with_middle_name(name):
    pattern = r'([\w \.-]*), ([\w \.-]*)$'
    result = re.search(pattern, name)
    if result is None:
        return "{}".format(name)
    return "{} {}".format(result[2], result[1])

print(rearranging_names_with_middle_name('Kapadia, Shreya Deepakkumar'))
print(rearranging_names_with_middle_name('Kapadia, Shivani Dipakkumar'))
print(rearranging_names_with_middle_name('Kapadia, Harshil D.'))
