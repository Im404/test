import os,platform
from up import main_apv
os.system('git pull -q')
ver = platform.architecture()[0]
if '64bit' in ver:
        main_apv()
else:
    exit('\n\n\n\033[1;31m Sorry, Your Device Not Support')
