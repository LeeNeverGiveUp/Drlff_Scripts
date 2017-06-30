import subprocess
from drlff.conf import env, files_input, files_output

pipe = subprocess.Popen(['garffield'], env=env)
print(env)
