#in cmd choose the path you want to install the package on using cd <PATH>
#then type:>>> python refresher_by.py py2exe

import os
a = os.getcwd()
path_package = '"'+a+'"'
try:
    os.system("easy_install pip")
except:
    pass
os.system('pip install '+path_package+'pyHook-1.5.1-cp27-cp27m-win_amd64 .whl')
os.system('pip install '+path_package+'py2exe-0.6.10a1-cp27-none-win_amd64.whl')
os.system("pip install pypiwin32")
os.system('pip install dropbox')
from distutils.core import setup
import py2exe

setup(
    windows = [
        {
            'py2exe': {
                "includes": [
                    "appdirs",
                    "ctypes",
                    "logging",
                    "OpenGL",
                    "PySide",
                    "PySide.QtUiTools",
           ], "excludes": [], "skip_archive":False, 'optimize': 2,
                "unbuffered": True, "bundle_files":2 },
            "script": "Refresher2.py",
            "icon_resources": [(1, "Watch_dogs.ico")]
        }
    ],
)