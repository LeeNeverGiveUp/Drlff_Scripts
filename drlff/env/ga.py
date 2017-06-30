import os
import subprocess
from drlff.conf import env, files_input, files_output

if not os.path.isdir('/tmp/ga'):
    if os.path.exists('/tmp/ga'):
        os.remove('/tmp/ga')
    os.mkdir('/tmp/ga')
os.chdir('/tmp/ga')

pipe = subprocess.Popen(
    [
    'garffield',
     files_input['geo'],
     files_input['ffield'],
     files_input['trainset'],
     files_input['params'],
    '-t 1',
        '-p 2:w'],
    env=env,
    stdout = subprocess.PIPE
)
print(env)
out, err = pipe.communicate()
print(out)
print(err)
with open()
