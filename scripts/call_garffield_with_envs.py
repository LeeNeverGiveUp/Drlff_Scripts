import subprocess
from conf import env

pipe = subprocess.Popen(['garffield', '$PATH'], env=env)
print(env)
