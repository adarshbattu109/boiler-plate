"""Constants to be used for Package Requirement Gathering and Setup"""
import os
from typing import Callable
from boilerplate.requirements import get_location, get_input, get_confirmation


OS = "WINDOWS" if os.name == "nt" else "UNIX"
"""`OS` constant will be used to determine how to drive the logic as per the OS"""

REQUIREMENTS_SEQUENCE: list[str] = ["BASE_DIR", "ROOT_DIR_NAME", "AUTHOR_NAME", "AUTHOR_EMAIL", "APP_NAME", "CREATE_ENV", "SCA", "LINTER", "FORMATTER", "UNIT_TEST"]
"""Sequence used for getting user preferences"""

EXECUTION_SEQUENCE: list[str] = ["CREATE_BASE_DIR", "CREATE_ROOT_DIR", "CREATE_SRC", "CREATE_APP_DIR", "CREATE_FILES", "CREATE_TEST_DIR", "CREATE_ENV", "INSTALL_PACKAGES"]
"""Sequence used for getting Setting up Files, Folders, Virtual Environement and Package preferences.
This shall work in tamdem with `REQUIREMENTS_SEQUENCE`"""

packages: dict[str, list] = {
    "SCA": ["flake8", "mypy", "dead", "vulture"],
    "LINTER": ["pylint"],
    # "FORMATTER": ["autopep8", "black", "isort", "yapf"],
    "FORMATTER": ["black"],
    "UNIT_TEST": ["pytest"],
}


requirement_steps: dict[str, tuple[Callable, str]] = {
    "BASE_DIR": (get_location, "Provide the Path of the directory where the project Root folder and other items will be placed : \n"),
    "ROOT_DIR_NAME": (get_input, "Provide the Project Root folder name ? : \n"),
    "AUTHOR_NAME": (get_input, "User Name ? : \n"),
    "AUTHOR_EMAIL": (get_input, "Email ID ? : \n"),
    "APP_NAME": (get_input, "Name of the Project ? : \n"),
    "CREATE_ENV": (get_confirmation, "Create Virtual Environment ? : \n"),
    "SCA": (get_confirmation, "Install Static Code Analysis Tools ? : \n"),
    "LINTER": (get_confirmation, "Install 'PyLint' ? : \n"),
    "FORMATTER": (get_confirmation, "Install 'Python Code Formatter' ? : \n"),
    "UNIT_TEST": (get_confirmation, "Install Unit Test Tools ? : \n"),
}
