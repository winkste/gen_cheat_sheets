# --- PYTHON Executable ---------------
# pyinstaller documentation: https://pyinstaller.org/en/stable/
# Install pyinstaller using pip
pip install pyinstaller

# simple way to create an executable
pyinstaller myscript.py

# create a single file executable
pyinstaller myscript.py -F

# Amount of detail in build-time console messages. 
# LEVEL: TRACE, DEBUG, INFO, WARN, ERROR, CRITICAL (default: INFO).
--log-level LEVEL

# A path to search for imports (like using PYTHONPATH). 
# Multiple paths are allowed, separated by ':'
-p DIR, --paths DIR

# run PyInstaller from Python code, 
# use the run function defined in PyInstaller.__main__. 
# For instance, the following code:

import PyInstaller.__main__

PyInstaller.__main__.run([
    'my_script.py',
    '--onefile',
    '--windowed'
])

# Run the command line based executables with
./name_of_exe

# manual configuration is also possible in the spec file
https://pyinstaller.org/en/stable/spec-files.html#using-spec-files




