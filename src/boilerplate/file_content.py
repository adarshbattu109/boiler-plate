"""File containing content for each file type"""

GIT_IGNORE = r"""
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
pip-wheel-metadata/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
.python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# PEP 582; used by e.g. github.com/David-OConnor/pyflow
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/
"""

PYPROJECT_TOML = r"""
[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"
"""

SETUP_PY = r"""
from setuptools import setup

if __name__ == "__main__":
    setup()
"""

SETUP_CFG = r"""
[metadata]
name = {APP_NAME}
version = 1.0
author = {AUTHOR_NAME}
author_email = {AUTHOR_EMAIL}
url = <Enter Project URL Here>
description = <Enter Project Description Here>
long_description = file: README.md
long_description_content_type = text/markdown
keywords = {APP_NAME}, setuptools
#license = BSD 3-Clause License
classifiers =
	Framework :: Custom
    #License :: BSD License
    Programming Language :: Python :: 3

[options]
python_requires = >= 3.9
package_dir=
    =src
packages=find:
zip_safe = True
include_package_data = False
install_requires =
    virtualenv

[options.packages.find]
where=src

[options.entry_points]
console_scripts = 
    boilerplate = boilerplate:main

[options.extras_require]
dev = 
    black
    flake8
	pylint
    vulture
	virtualenv
test = 
	pytest
	mypy
	flake8
	coverage
	pytest-cov
	pylint
	black

[flake8]
exclude = .tox,*.egg,build,__pycache__,htmlcov,venv
select = E,W,F
ignore = E501
show_source = True
statistics = True

[mypy]
ignore_missing_imports = True

[tool:pytest]
addopts = -v --cov={APP_NAME} --cov-report=html
filterwarnings = ignore::DeprecationWarning"""

README_MD = r"""
## Authors

- [@{AUTHOR_NAME}](https://github.com/)


## Installation

Create a Virtual Environment

```bash
  # Install the virtualenv module
  pip install virtualenv

  # Create the virtual Environment named venv
  python -m venv venv
  or
  virtualenv venv

  # Activate the Virtual Environment
  venv\Scripts\activate
```
    
Install the Application

```bash
  # Install the {APP_NAME} app
  pip install -e .
```

Install the Extras

```bash
  # Install the Extras for Dev and Test
  pip install -e ".[dev, test]"
```

## Running Tests

To run the tests, refer the following

 - Flake8
  ```bash
  flake8 src test
  ```
 - Pytest
  ```bash
  pytest -v
  ```
 - mypy
  ```bash
  mypy src test
  ```
 - pylint
  ```bash
  pylint src test
  ```
 - vulture
  ```bash
  vulture src test
  ```"""
