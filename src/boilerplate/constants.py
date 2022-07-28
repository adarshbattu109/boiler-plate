"""Constants to be used for Package Requirement Gathering and Setup"""

from typing import Callable
from boilerplate.file_content import GIT_IGNORE, PYPROJECT_TOML, README_MD, SETUP_CFG, SETUP_PY
from boilerplate.requirements import get_location, get_input, get_confirmation


# OS = "WINDOWS" if os.name == "nt" else "UNIX"
# """`OS` constant will be used to determine how to drive the logic as per the OS"""

REQUIREMENTS_SEQUENCE: list[str] = ["BASE_DIR", "ROOT_DIR_NAME", "AUTHOR_NAME", "AUTHOR_EMAIL", "APP_NAME", "CREATE_ENV", "SCA", "LINTER", "FORMATTER", "UNIT_TEST"]
"""Sequence used for getting user preferences"""

# EXECUTION_SEQUENCE: list[str] = ["GET_BASE_DIR", "CREATE_ROOT_DIR", "CREATE_SRC", "CREATE_TEST_DIR", "CREATE_APP_DIR", "CREATE_FILES", "SETUP_ENV_INSTALL_PACKAGES"]
# """Sequence used for getting Setting up Files, Folders, Virtual Environement and Package preferences.
# This shall work in tamdem with `REQUIREMENTS_SEQUENCE`"""

packages: dict[str, list] = {
    "SCA": ["flake8", "mypy", "vulture"],
    "LINTER": ["pylint"],
    # "FORMATTER": ["autopep8", "black", "isort", "yapf"],
    "FORMATTER": ["black"],
    "UNIT_TEST": ["pytest"],
}


requirement_steps: dict[str, tuple[Callable, str]] = {
    "BASE_DIR": (get_location, "Provide the Path of the directory where the project Root folder and other items will be placed : "),
    "ROOT_DIR_NAME": (get_input, "Provide the Project Root folder name ? : "),
    "AUTHOR_NAME": (get_input, "User Name ? : "),
    "AUTHOR_EMAIL": (get_input, "Email ID ? : "),
    "APP_NAME": (get_input, "Name of the Project ? : "),
    "CREATE_ENV": (get_confirmation, "Create Virtual Environment ? : "),
    "SCA": (get_confirmation, "Install Static Code Analysis Tools ? : "),
    "LINTER": (get_confirmation, "Install 'PyLint' ? : "),
    "FORMATTER": (get_confirmation, "Install 'Python Code Formatter' ? : "),
    "UNIT_TEST": (get_confirmation, "Install Unit Test Tools ? : "),
}

# execution_steps: dict[str, tuple[Callable, str | Path | list[str]]] = {
#     "GET_BASE_DIR": (Path,"")
#     "CREATE_ROOT_DIR": (create_directory)
#     "CREATE_SRC": create_directory,
#     "CREATE_TEST_DIR": create_directory,
#     "CREATE_APP_DIR": create_directory,
#     "CREATE_FILES": create_file,
#     "SETUP_ENV_INSTALL_PACKAGES": create_vitual_env_with_packages,
# }

# FILE_NAME_LIST = [".gitignore", "pyproject.toml", "setup.cfg", "setup.py", "README.md"]
FILE_CONTENT_DICT: dict[str, str] = {".gitignore": GIT_IGNORE, "pyproject.toml": PYPROJECT_TOML, "setup.py": SETUP_PY, "setup.cfg": SETUP_CFG, "README.md": README_MD}
