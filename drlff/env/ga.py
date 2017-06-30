import os
import subprocess
from drlff.conf import env, files_input, files_output, example_input_path

def run():
    if not os.path.isdir(files_output['log']):
        if os.path.exists(files_output['log']):
            os.remove(files_output['log'])
        os.mkdir(files_output['log'])

    os.chdir(example_input_path)
    pipe = subprocess.Popen(
        [
            'garffield',
            'geo.new',
            'ffield',
            'trainset.in.new',
            'params',
            #files_input['geo'],
            #files_input['ffield'],
            #files_input['trainset'],
            #files_input['params'],
            '-t','1',
            '-p','2'],
        env=env,
        stdout=subprocess.PIPE
    )
    out, err = pipe.communicate()
    with open(os.path.join(files_output['log'], 'drlff.ga.log'), 'a') as f:
        f.write(out.decode('utf-8'))
    return files_output['log']
