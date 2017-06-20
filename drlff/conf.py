# Environment variables, including running path of garffield, mpich, etc, and library of garffield.
env = {
    'PATH': '/home/charlesxu/Workspace/softs/garffield/mpich/bin:/home/charlesxu/Workspace/softs/garffield/bin:/home/charlesxu/Workspace/softs/garffield/mpich/bin:/home/charlesxu/Workspace/softs/garffield/bin:/home/charlesxu/anaconda3/bin:/home/charlesxu/.userscripts:/home/charlesxu/.fzf/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games',
    'LD_LIBRARY_PATH': '/opt/intel/compilers_and_libraries_2017.2.174/linux/compiler/lib/intel64_lin_mic/:/opt/intel/compilers_and_libraries_2017.2.174/linux/compiler/lib/intel64_lin:/home/charlesxu/Workspace/softs/garffield/lib:/home/charlesxu/Workspace/softs/garffield/fftw/lib:/home/charlesxu/Workspace/softs/garffield/mpich/lib:/opt/intel/compilers_and_libraries_2017.2.174/linux/compiler/lib/intel64_lin_mic/:/opt/intel/compilers_and_libraries_2017.2.174/linux/compiler/lib/intel64_lin:/home/charlesxu/Workspace/softs/garffield/lib:/home/charlesxu/Workspace/softs/garffield/fftw/lib:/home/charlesxu/Workspace/softs/garffield/mpich/lib'}

# files_input = {
#         'geo': '/home/charlesxu/Workspace/softs/GARFfield/test/reax/Cl2/unweighted/MPE/geo.new',
#         'ffield': '/home/charlesxu/Workspace/softs/GARFfield/test/reax/Cl2/unweighted/MPE/ffield',
#         'trainset.in': '/home/charlesxu/Workspace/softs/GARFfield/test/reax/Cl2/unweighted/MPE/trainset.in.new',
#         'params': '/home/charlesxu/Workspace/softs/GARFfield/test/reax/Cl2/unweighted/MPE/params'
#         }

files_input = {
    'geo': '/home/charles/Workspace/official/drlff/resources/MPE/geo.new',
    'ffield': '/home/charles/Workspace/official/drlff/resources/MPE/ffield',
    'trainset.in': '/home/charles/Workspace/official/drlff/resources/MPE/trainset.in.new',
    'params': '/home/charles/Workspace/official/drlff/resources/MPE/params'
}

files_output = {
    'log': '~/.cache/drlff.log'
}
