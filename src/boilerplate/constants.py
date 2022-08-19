"""Constants to be used for Package Requirement Gathering and Setup"""

from typing import Callable
from boilerplate.file_content import GIT_IGNORE, PYPROJECT_TOML, README_MD, SETUP_CFG, SETUP_PY
from boilerplate.messages import APP_NAME_MSG, AUTHOR_EMAIL_MSG, AUTHOR_NAME_MSG, BASE_DIR_MSG, FINAL_CONF_MSG, FORMATTER_MSG, LINTER_MSG, ROOT_DIR_NAME_MSG, SCA_MSG, UNIT_TEST_MSG
from boilerplate.cli import get_location, get_input, get_confirmation, get_selection_from_choices, get_multi_select_choices


FILE_CONTENT_DICT: dict[str, str] = {".gitignore": GIT_IGNORE, "pyproject.toml": PYPROJECT_TOML, "setup.py": SETUP_PY, "setup.cfg": SETUP_CFG, "README.md": README_MD}


REQUIREMENTS_SEQUENCE: list[str] = ["BASE_DIR", "ROOT_DIR_NAME", "AUTHOR_NAME", "AUTHOR_EMAIL", "APP_NAME", "SCA", "LINTER", "FORMATTER", "UNIT_TEST", "FINAL_CONF"]
"""Sequence used for getting user preferences"""

packages: dict[str, list] = {
    "SCA": ["flake8", "mypy", "vulture"],
    "LINTER": ["pylint"],
    "FORMATTER": ["autopep8", "black", "isort", "yapf"],
    "UNIT_TEST": ["pytest"],
}

requirement_steps: dict[str, tuple[Callable, dict]] = {
    "BASE_DIR": (get_location, {"message": BASE_DIR_MSG}),
    "ROOT_DIR_NAME": (get_input, {"message": ROOT_DIR_NAME_MSG}),
    "AUTHOR_NAME": (get_input, {"message": AUTHOR_NAME_MSG}),
    "AUTHOR_EMAIL": (get_input, {"message": AUTHOR_EMAIL_MSG}),
    "APP_NAME": (get_input, {"message": APP_NAME_MSG}),
    "SCA": (get_multi_select_choices, {"message": SCA_MSG, "choices": packages["SCA"]}),
    "LINTER": (get_confirmation, {"message": LINTER_MSG}),
    "FORMATTER": (get_selection_from_choices, {"message": FORMATTER_MSG, "choices": packages["FORMATTER"]}),
    "UNIT_TEST": (get_confirmation, {"message": UNIT_TEST_MSG}),
    "FINAL_CONF": (get_confirmation, {"message": FINAL_CONF_MSG}),
}
