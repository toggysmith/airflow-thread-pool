# This script assumes that 'doxygen' is available in PATH.

import subprocess
import os
import sys

was_internal_flag_passed = False
if len(sys.argv) > 1 and sys.argv[1] == "--internal":
        was_internal_flag_passed = True

custom_env = os.environ.copy()
if was_internal_flag_passed:
    custom_env["DOXYGEN_INPUT"] = "../src ../include"
else:
    custom_env["DOXYGEN_INPUT"] = "../include"

python_script_location = os.path.dirname(os.path.realpath(__file__))
os.chdir(python_script_location + "/../docs")

subprocess.run(["doxygen", "../docs/Doxyfile"], env = custom_env)
