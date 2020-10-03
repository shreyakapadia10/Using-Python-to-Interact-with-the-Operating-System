import subprocess

result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
print(result.returncode)
print(result.stdout)
print(result.stdout.decode().split())

result = subprocess.run(["rm", "no_such_file"], capture_output=True)
print(result.returncode)
print(result.stdout)
print(result.stderr)
