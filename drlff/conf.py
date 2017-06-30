import os

conf_path = os.path.abspath(__file__)
conf_dir = os.path.split(conf_path)[0]

example_input_path = os.path.join(conf_dir, '../resources/MPE/')
# Environment variables, including running path of garffield, mpich, etc, and library of garffield.
env = {
    'PATH': '/home/charlesxu/Workspace/softs/garffield/mpich/bin:/home/charlesxu/Workspace/softs/garffield/bin:/home/charlesxu/Workspace/softs/garffield/mpich/bin:/home/charlesxu/Workspace/softs/garffield/bin:/home/charlesxu/anaconda3/bin:/home/charlesxu/.userscripts:/home/charlesxu/.fzf/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games',
    'LD_LIBRARY_PATH': '/opt/intel/compilers_and_libraries_2017.2.174/linux/compiler/lib/intel64_lin_mic/:/opt/intel/compilers_and_libraries_2017.2.174/linux/compiler/lib/intel64_lin:/home/charlesxu/Workspace/softs/garffield/lib:/home/charlesxu/Workspace/softs/garffield/fftw/lib:/home/charlesxu/Workspace/softs/garffield/mpich/lib:/opt/intel/compilers_and_libraries_2017.2.174/linux/compiler/lib/intel64_lin_mic/:/opt/intel/compilers_and_libraries_2017.2.174/linux/compiler/lib/intel64_lin:/home/charlesxu/Workspace/softs/garffield/lib:/home/charlesxu/Workspace/softs/garffield/fftw/lib:/home/charlesxu/Workspace/softs/garffield/mpich/lib'}
# conf.titan
# files_input = {
#         'geo': '/home/charlesxu/Workspace/softs/GARFfield/test/reax/Cl2/unweighted/MPE/geo.new',
#         'ffield': '/home/charlesxu/Workspace/softs/GARFfield/test/reax/Cl2/unweighted/MPE/ffield',
#         'trainset': '/home/charlesxu/Workspace/softs/GARFfield/test/reax/Cl2/unweighted/MPE/trainset.in.new',
#         'params': '/home/charlesxu/Workspace/softs/GARFfield/test/reax/Cl2/unweighted/MPE/params'
#         }

# conf.lenovo
# files_input = {
#     'geo': '/home/charles/Workspace/official/drlff/resources/MPE/geo.new',
#     'ffield': '/home/charles/Workspace/official/drlff/resources/MPE/ffield',
#     'trainset': '/home/charles/Workspace/official/drlff/resources/MPE/trainset.in.new',
#     'params': '/home/charles/Workspace/official/drlff/resources/MPE/params'
# }

# conf.mipad
# files_input = {
#     'geo': '/data/data/com.termux/files/home/Gits/drlff/data/MPE/geo.new',
#     'ffield': '/data/data/com.termux/files/home/Gits/drlff/data/MPE/ffield',
#     'trainset': '/data/data/com.termux/files/home/Gits/drlff/data/MPE/trainset.in.new',
#     'params': '/data/data/com.termux/files/home/Gits/drlff/data/MPE/params'
# }

# conf.generic
files_input = {
    'geo': os.path.join(example_input_path, 'geo.new'),
    'ffield': os.path.join(example_input_path, 'ffield'),
    'trainset': os.path.join(example_input_path, 'trainset.in.new'),
    'params': os.path.join(example_input_path, 'params')
}

files_output = {
    'log': '~/.cache/drlff.log'
}
