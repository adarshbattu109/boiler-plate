"""This Program will create a seed Boiler plate as per user prefereces"""

from pathlib import Path
from boilerplate.file_content import MAIN_INIT_PY
from boilerplate.messages import SUCCESS_MSG
from boilerplate.constants import FILE_CONTENT_DICT, REQUIREMENTS_SEQUENCE
from boilerplate.constants import requirement_steps, packages
from boilerplate.helper import create_directory, touch_file, create_repo_files, create_vitual_env_with_packages


def gather_requirements() -> dict[str, str]:
    """Method to gather user requirements for setting up a new project"""
    user_inputs: dict = {}
    for requirement in REQUIREMENTS_SEQUENCE:
        function, function_args = requirement_steps[requirement]
        user_inputs[requirement] = function(**function_args)
    return user_inputs


def execute_steps(user_inputs: dict[str, str]) -> None:
    """Since the user input in captured in a structured way, each item in the list can be used to execute the needful steps"""

    directory_paths: list[Path] = []

    main_path = Path(user_inputs["BASE_DIR"], user_inputs["ROOT_DIR_NAME"])
    app_name = user_inputs["APP_NAME"]
    directory_paths.append(main_path)
    directory_paths.append(Path(main_path, "src"))
    directory_paths.append(Path(main_path, "test"))
    directory_paths.append(Path(main_path, "src", f"{app_name}"))

    # Create Directories
    for directory_path in directory_paths:
        create_directory(path=directory_path)

    file_paths: list[Path] = []
    # Create Files
    file_paths.append(Path(main_path, "src", "__init__.py"))
    file_paths.append(Path(main_path, "src", f"{app_name}", "__init__.py"))
    file_paths.append(Path(main_path, "test", "__init__.py"))

    # Create Module by adding __init__.py
    for file_path in file_paths:
        touch_file(path=file_path)

    # Update the content of the __init__.py file to be called by calling the app module
    # to-do: Update this concept with a function to consume file to be created, file_path, file_content
    with open(Path(main_path, "src", f"{app_name}", "__init__.py"), "w", encoding="utf8") as filehandle:
        filehandle.write(MAIN_INIT_PY)

    # Create the repo files for installation and setup with substitutions
    for file_type in FILE_CONTENT_DICT:
        file_name = Path(main_path, file_type)
        create_repo_files(file_type=file_type, file=file_name, substitution_dict=user_inputs)

    package_list: list[str] = []
    if user_inputs["SCA"]:
        package_list.extend(user_inputs["SCA"])
    if user_inputs["LINTER"]:
        package_list.extend(packages["LINTER"])
    if user_inputs["FORMATTER"]:
        package_list.extend([user_inputs["FORMATTER"]])
    if user_inputs["UNIT_TEST"]:
        package_list.extend(packages["UNIT_TEST"])

    return_state = create_vitual_env_with_packages(venv_path=main_path, packages=package_list)

    if not return_state:
        print(SUCCESS_MSG)
