import re
def rearranging_names(name):
    pattern = r'^([\w \.-]*), ([\w \.-]*)$'
    result = re.search(pattern, name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])
