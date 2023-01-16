import os
from subprocess import Popen

BASEDIR = os.path.abspath(os.getcwd())
_env = "venv"
venv_py = f"{_env}/Scripts/python"

if __name__ == '__main__':
    if not os.path.exists(os.path.join(BASEDIR, "venv")):
        print(f"Creating virtual environment : {_env}")
        init = Popen(f"python -m venv {_env}".split()).communicate()
        print("Checking for new pip && wheel versions... last security version.")
        check_pip = Popen(f"{venv_py} -m pip install --upgrade pip".split()).communicate()
        check_wheel = Popen(f"{venv_py} -m pip install --upgrade wheel".split()).communicate()
        if not os.path.exists(os.path.join(BASEDIR, _env)):
            raise EnvironmentError("You must setup a virtual environment to use this method.\n"
                                   f">>> python venv {_env}\n>>> activate\n"
                                   ">>>pip install -r requirements.txt")
    if os.path.exists(os.path.join(BASEDIR, _env)):
        print("Applying requirements")
        install = Popen(f"{venv_py} -m pip install -r requirements.txt".split()).communicate()
