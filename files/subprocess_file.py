
import subprocess

result = subprocess.run('dir', shell=True)
print(result.stderr)


