import os
import re
import subprocess
from drlff.conf import env, files_input, files_output


def get_error(path):
    with open(path, 'r') as f:
        data = f.readlines()

    return float(re.findall('[\d\.]+', data[-1])[0])


def run():
    if not os.path.isdir(files_output['log']):
        if os.path.exists(files_output['log']):
            os.remove(files_output['log'])
        os.mkdir(files_output['log'])

    os.chdir(files_input['dir'])
    pipe = subprocess.Popen(
        ['garffield',
            files_input['geo'],
            files_input['ffield'],
            files_input['trainset'],
            files_input['params'],
            '-t', '1',
            '-p', '2'],
        env=env,
        stdout=subprocess.PIPE
    )
    out, err = pipe.communicate()
    pipe.terminate()
    del pipe
    with open(os.path.join(files_output['log'], 'drlff.ga.log'), 'a') as f:
        f.write(out.decode('utf-8'))
    return get_error(os.path.join(files_input['dir'], 'trainset.err.initial'))
