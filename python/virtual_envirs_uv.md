
## Installing UV

UV can be installed system-wide using cURL on macOS and Linux:
```
$ curl -LsSf https://astral.sh/uv/install.sh | sudo sh
```
 
And with Powershell on Windows (make sure you run Powershell with administrator privileges):
```
$ powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

UV is available via Homebrew as well:
```
$ brew install uv
```


you can verify the installation by running uv version:
```
$ uv version
uv 0.4.25 (97eb6ab4a 2024-10-21)
```

## Initializing a new project

Working on projects is the core part of the UV experience. You start by initializing an empty project using the uv init command:

```
$ uv init explore-uv
Initialized project explore-uv at /Users/bexgboost/projects/explore-uv
```

The command will immediately create a new explore-uv directory with the following contents:
```
$ cd explore-uv
$ tree -a
.
├── .gitignore
├── .python-version
├── README.md
├── hello.py
└── pyproject.toml
```

## Adding initial dependencies to the project

UV combines the environment creation and dependency installation into a single command - uv add:
```
$ uv add scikit-learn xgboost
Using CPython 3.9.20 interpreter at: /opt/homebrew/opt/python@3.9/bin/python3.9
Creating virtual environment at: .venv
Resolved 6 packages in 1.78s
⠧ Preparing packages... (2/5)
Prepared 5 packages in 1m 23s
Installed 5 packages in 45ms
 + joblib==1.4.2
 + numpy==2.0.2
 + scikit-learn==1.5.2
 ...
 ```

 To remove a dependency from the environment and the pyproject.toml file, you can use the uv remove command. It will uninstall the package and all its child-dependencies:
```
$ uv remove scikit-learn
```

## Running Python scripts
To run a Python script directly, you can use the uv run command followed by your script name instead of the usual python script.py syntax:
```
$ uv run hello.py
```

## Listing existing Python versions
```
$ uv python list --only-installed
```

## Changing Python versions for the current project 

You can switch Python versions for your current UV project at any point as long as the new version satisfies the specifications in your pyproject.toml file. For example, the following file requires Python versions 3.9 and above:
```
...
requires-python = ">=3.9"
```
This means you can change the Python version in .***python-version file*** to any version above, like 3.11.7. Afterwards, call:
```
uv sync
```
ensure that all dependencies are reinstalled with:
```
$ uv pip install -e .
```

## How to run uv tools?
1. Using uv tool run:
```
$ uv tool run black hello.py
```
2. Using the shorter and more convenient uvx command:
```
$ uvx black hello.py
```

## Generate a requirements.txt file from the uv.lock file:
```
$ uv export -o requirements.txt
```
## Special dependencies management

1. Installing the latest version of a package:
```
$ uv add requests
```

2. Installing a specific version:
```
$ uv add requests=2.1.2
```

3. Change the bounds of a package's constraints:
```
$ uv add 'requests<3.0.0'
```

4. Make a dependency platform-specific:
```
$ uv add 'requests; sys_platform="linux"'
```
| pip/virtualenv | UV equivalent |
|----------------|---------|
|python -m venv .venv|uv venv|
|pip install package|uv add package|
|pip install -r requirements.txt|uv pip install -r requirements.txt|
|pip uninstall package|uv remove package|
|pip freeze|uv pip freeze|
|pip list|uv pip list|


