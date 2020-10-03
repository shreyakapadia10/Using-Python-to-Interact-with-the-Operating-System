import os
import subprocess

my_env = os.environ.copy()
print("Before: ")
print(my_env['PATH'])

my_env['PATH'] = os.pathsep.join(["/opt/myapp" , my_env["PATH"]])

print("After: ")
print(my_env['PATH'])

result = subprocess.run(["adding_one_more_path_to_env"], env=my_env)
