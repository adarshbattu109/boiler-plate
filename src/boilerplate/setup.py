"""This library will help setup all the User preferences and Directory structure"""

import os
from pathlib import Path

from boilerplate.constants import FILE_CONTENT_DICT


def create_directory(path: Path) -> None:
    """_summary_

    Args:
        path (Path): _description_
    """
    print(f"Creating Directory {path}")
    path.mkdir(parents=True, exist_ok=True)


def touch_file(path: Path) -> None:
    """_summary_

    Args:
        path (Path): _description_
    """
    print(f"Creating file {path}")
    path.touch()


def create_repo_files(file_type: str, file: Path, substitution_dict: dict[str, str]) -> None:
    """Method to copy over file from local store to new project with content substitution

    Args:
        file_type (str): Dict key to derive the file to read for substitution
        file (Path): Target path to write the file to
    """
    content = FILE_CONTENT_DICT[file_type]
    for key, value in substitution_dict.items():
        content = content.replace(str(key), str(value))

    print(f"Creating file {file}")
    with open(file, "w", encoding="utf8") as filehandle:
        filehandle.write(content)


def create_vitual_env_with_packages(venv_path: Path, packages: list[str]) -> None:
    """_summary_

    Args:
        packages (list[str]): List of Packages to be installed
    """

    final_command = []
    concat_string = "&&" if os.name == "nt" else ";"
    activate_venv = str(Path(".", "venv", "Scripts", "activate"))
    start_cmd = [f"cd {venv_path}", 'echo "Starting Virtual Environment Setup"']
    create_virtual_env = ["pip install -U virtualenv", "python -m virtualenv venv", activate_venv]
    install_project = ["pip install -e ."]

    final_command.extend(start_cmd)
    final_command.extend(create_virtual_env)

    for package in packages:
        final_command.append(f"pip install -U {package}")

    final_command.extend(install_project)

    final = f"{concat_string}".join(final_command)
    os.system(final)
