"""Constants to be used for Package Requirement Gathering and Setup"""

from boilerplate.file_content import GIT_IGNORE, PYPROJECT_TOML, README_MD, SETUP_CFG, SETUP_PY
from boilerplate.cli import get_location, get_input, get_confirmation, get_selection_from_choices, get_multi_select_choices


FILE_CONTENT_DICT: dict[str, str] = {".gitignore": GIT_IGNORE, "pyproject.toml": PYPROJECT_TOML, "setup.py": SETUP_PY, "setup.cfg": SETUP_CFG, "README.md": README_MD}


REQUIREMENTS_SEQUENCE: list[str] = ["BASE_DIR", "ROOT_DIR_NAME", "AUTHOR_NAME", "AUTHOR_EMAIL", "APP_NAME", "CREATE_ENV", "SCA", "LINTER", "FORMATTER", "UNIT_TEST", "FINAL_CONF"]
"""Sequence used for getting user preferences"""

packages: dict[str, list] = {
    "SCA": ["flake8", "mypy", "vulture"],
    "LINTER": ["pylint"],
    "FORMATTER": ["autopep8", "black", "isort", "yapf"],
    "UNIT_TEST": ["pytest"],
}

requirement_steps: dict[str, dict[str, str]] = {
    "BASE_DIR": (get_location, {"message": "Provide the Path of the directory where the project Root folder and other items will be placed : "}),
    "ROOT_DIR_NAME": (get_input, {"message": "Provide the Project Root folder name ? : "}),
    "AUTHOR_NAME": (get_input, {"message": "User Name ? : "}),
    "AUTHOR_EMAIL": (get_input, {"message": "Email ID ? : "}),
    "APP_NAME": (get_input, {"message": "Name of the Project ? : "}),
    "CREATE_ENV": (get_confirmation, {"message": "Create Virtual Environment ? : "}),
    "SCA": (get_multi_select_choices, {"message": "Install Static Code Analysis Tools ? : ", "choices": packages["SCA"]}),
    "LINTER": (get_confirmation, {"message": "Install 'PyLint' ? : "}),
    "FORMATTER": (get_selection_from_choices, {"message": "Install 'Python Code Formatter' ? : ", "choices": packages["FORMATTER"]}),
    "UNIT_TEST": (get_confirmation, {"message": "Install `PyTest`? : "}),
    "FINAL_CONF": (get_confirmation, {"message": "Proceed with Installation ? : "}),
}
