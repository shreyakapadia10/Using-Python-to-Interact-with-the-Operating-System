# import re for regular r=expression
import re

# r indicates rawstring thus it is told that python should not try to interprete it
result = re.search(r'aza', 'plaaza')
print("result = re.search(r'aza', 'plaaza') = ", result)

result = re.search(r'aza', 'maazaa')
print("result = re.search(r'aza', 'maazaa') = ", result)

# returns None if pattern doesn't match
result = re.search(r'aza', 'maze')
print("result = re.search(r'aza', 'maazaa') = ", result)

# '^' represent starting of line
result = re.search(r'^m', 'maazaa')
print("result = re.search(r'^m', 'maazaa') = ",result)

result = re.search(r'p.ng', 'penguine')
print("result = re.search(r'p.ng', 'Penguine') = ", result)

result = re.search(r'p.ng', 'Sponge')
print("result = re.search(r'p.ng', 'Sponge') = ", result)

result = re.search(r'p.ng', 'Clapping')
print("result = re.search(r'p.ng', 'Clapping') = ", result)

result = re.search(r'p.ng', 'SPONGE',re.IGNORECASE)
print("result = re.search(r'p.ng', 'SPONGE',re.IGNORECASE()) = ", result)
