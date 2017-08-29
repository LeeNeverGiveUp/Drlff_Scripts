import os

conf_path = os.path.abspath(__file__)
conf_dir = os.path.split(conf_path)[0]

example_input_path = os.path.abspath(os.path.join(conf_dir, '../resources/MPE/'))
# Environment variables, including running path of garffield, mpich, etc, and library of garffield.
env = {
    'PATH': '/home/charlesxu/Workspace/softs/garffield/mpich/bin:/home/charlesxu/Workspace/softs/garffield/bin:/home/charlesxu/Workspace/softs/garffield/mpich/bin:/home/charlesxu/Workspace/softs/garffield/bin:/home/charlesxu/anaconda3/bin:/home/charlesxu/.userscripts:/home/charlesxu/.fzf/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games',
    'LD_LIBRARY_PATH': '/opt/intel/compilers_and_libraries_2017.2.174/linux/compiler/lib/intel64_lin_mic/:/opt/intel/compilers_and_libraries_2017.2.174/linux/compiler/lib/intel64_lin:/home/charlesxu/Workspace/softs/garffield/lib:/home/charlesxu/Workspace/softs/garffield/fftw/lib:/home/charlesxu/Workspace/softs/garffield/mpich/lib:/opt/intel/compilers_and_libraries_2017.2.174/linux/compiler/lib/intel64_lin_mic/:/opt/intel/compilers_and_libraries_2017.2.174/linux/compiler/lib/intel64_lin:/home/charlesxu/Workspace/softs/garffield/lib:/home/charlesxu/Workspace/softs/garffield/fftw/lib:/home/charlesxu/Workspace/softs/garffield/mpich/lib'}

files_input = {
    'dir': example_input_path,
    'geo': 'geo.new',
    'ffield': 'ffield',
    'trainset': 'trainset.in.new',
    'params': 'params'
}

files_output = {
    'log': os.path.expanduser('~/.cache/ga')
}
