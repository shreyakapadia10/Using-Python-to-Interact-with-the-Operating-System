import os
import subprocess

my_env = os.environ.copy()
print("Before: ")
print(my_env['PATH'])

my_env['PATH'] = os.pathsep.join(["E:\Shreya\Diploma\Self Learning\Python\Course2\Module4" , my_env["PATH"]])

print("After: ")
print(my_env['PATH'])

result = subprocess.run(["adding_one_more_path_to_env"], env=my_env)
