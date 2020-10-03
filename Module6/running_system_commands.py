import subprocess

subprocess.run(["date"])

print("subprocess.run(['sleep', '2']) will wait for 2 seconds")
subprocess.run(["sleep", "2"])

print("Trying to list a file that doesn't exist using ls")
result = subprocess.run(["ls", "no_such_file.txt"])
print(result.returncode)
