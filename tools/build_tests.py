# This script assumes that 'cmake' is available in PATH.

import subprocess
import os

python_script_location = os.path.dirname(os.path.realpath(__file__))
os.chdir(python_script_location + "/..")

try:
    _ = subprocess.run(["cmake", "-B", "build", "-DBUILD_TESTS=ON"]).check_returncode()
except subprocess.CalledProcessError:
    print("Error: Attempt to generate build files failed. Exiting early.")
    exit()

try:
    _ = subprocess.run(["cmake", "--build", "build"]).check_returncode()
except subprocess.CalledProcessError:
    print("Error: Attempt to build using build files failed. Exiting early.")
    exit()
