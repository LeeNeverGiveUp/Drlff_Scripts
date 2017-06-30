import subprocess
from drlff.conf import env, files_input, files_output

pipe = subprocess.Popen(
    ['garffield',
     files_input['geo'],
     files_input['ffield'],
     files_input['trainset'],
     files_input['params']],
    env=env)
print(env)
pipe.wait()
