import os
import subprocess

my_env = os.environ.copy()
print("Before: ")
print(my_env['PATH'])

my_env['PATH'] = os.pathsep.join(["/Desktop/Shreya/Python" , my_env["PATH"]])

print("After: ")
print(my_env['PATH'])

result = subprocess.run(["myapp"], env=my_env)
