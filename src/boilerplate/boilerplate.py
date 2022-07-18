"""This Program will create a seed Boiler plate as per user prefereces"""

from pathlib import Path
from boilerplate.constants import REQUIREMENTS_SEQUENCE
from boilerplate.constants import requirement_steps, packages
from boilerplate.setup import create_directory, create_file, create_vitual_env_with_packages


def gather_requirements() -> list:
    """Method to gather user requirements for setting up a new project"""
    user_inputs: list = []
    for requirement in REQUIREMENTS_SEQUENCE:
        function, message = requirement_steps[requirement]
        user_input = function(message)
        user_inputs.append(user_input)
    return user_inputs


def execute_steps(user_inputs: list) -> None:
    """Since the user input in captured in a structured way, each item in the list can be used to execute the needful steps"""
    # todo: Develop robust mechanism to deal with sequence change
    base_dir, root_dir, author_name, author_email, app_name = user_inputs[0:5]
    install_venv, install_sca, install_linter, install_formatter, install_unit_test = user_inputs[5:]

    # print(f"{base_dir}, {root_dir}, {author_name}, {author_email}, {app_name}")
    # print(f"{install_venv}, {install_sca}, {install_linter}, {install_formatter}, {install_unit_test}")

    directory_paths = []
    directory_paths.append(Path(base_dir, root_dir))
    directory_paths.append(Path(base_dir, root_dir, "src"))
    directory_paths.append(Path(base_dir, root_dir, "test"))
    directory_paths.append(Path(base_dir, root_dir, "src", f"{app_name}"))
    # Create Directories
    for directory_path in directory_paths:
        create_directory(path=directory_path)

    # Create Files
    file_paths = []
    file_paths.append(Path(base_dir, root_dir, "src", "__init__.py"))
    file_paths.append(Path(base_dir, root_dir, "src", f"{app_name}", "__init__.py"))
    file_paths.append(Path(base_dir, root_dir, "test", "__init__.py"))
    # Create Moudule by adding __init__.py
    for file_path in file_paths:
        create_file(path=file_path)

    # todo : Copy over files from data to new repo & make changes to Files
    # shutil.copy()
    # Path(base_dir, root_dir)
    print(f"Author Name: {author_name}, Email ID: {author_email}")

    package_list = []
    if install_sca:
        package_list.extend(packages["SCA"])
    if install_linter:
        package_list.extend(packages["LINTER"])
    if install_formatter:
        package_list.extend(packages["FORMATTER"])
    if install_unit_test:
        package_list.extend(packages["UNIT_TEST"])

    # todo: Fix this always true condition
    if install_venv or True:
        path = Path(base_dir, root_dir)
        create_vitual_env_with_packages(venv_path=path, packages=package_list)
