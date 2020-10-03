import os

print("PATH: " + os.environ.get("PATH", ""))
print("HOMEPATH: " + os.environ.get("HOMEPATH", ""))
print("FRUIT: " + os.environ.get("FRUIT", ""))
# In Linux we can write export FRUIT=anyValue so that value of FRUIT will also be printed
