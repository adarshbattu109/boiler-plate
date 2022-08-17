"""This File contains all the methods required to capture user preferences to setup the project"""

import os
from pathlib import Path
from InquirerPy import inquirer
from InquirerPy.validator import PathValidator


def get_location(message: str) -> Path:
    """Method to get `Directory` location from the end user

    Args:
        message (str): Message to display to the user as prompt

    Returns:
        Path: Path provided by the user
    """
    home_path = "~/" if os.name == "posix" else "C:\\"
    location = inquirer.filepath(
        default=home_path,
        message=message,
        validate=PathValidator(is_dir=True, message="Input is not a directory"),
        only_directories=True,
    ).execute()
    return Path(location)


def get_input(message: str) -> str:
    """Method to get User Input from the User as String

    Args:
        message (str): Message to show to the user

    Returns:
        str: Input provided by the end-user as `string`
    """
    return inquirer.text(message=f"{message}").execute()


def get_confirmation(message: str) -> bool:
    """Method to get confirmation on against the displayed message

    Args:
        message (str): Message to show to the user
        selection (bool): User Preference agains

    Returns:
        bool: Final preference by user against the displayed message
    """
    return inquirer.confirm(message=message, default=False).execute()


def get_selection_from_choices(message: str, choices: list[str]) -> str:
    """Method to get single user selection from list of available choices

    Args:
        message (str): Message to show to the user
        choices (list[str]): List of choices to showcase

    Returns:
        str: selection made by the user
    """
    # choices = choices.append(Choice(value=None, name="Exit"))
    choice = inquirer.select(
        message=message,
        choices=choices,
        default=None,
    ).execute()

    return choice


def get_multi_select_choices(message: str, choices: list[str]) -> list[str]:
    """Method to get multiple user selection from list of available choices

    Args:
        message (str): Message to show to the user
        choices (list[str]): List of choices to showcase

    Returns:
        list[str]: List of selections made by the user
    """
    selection = inquirer.checkbox(
        message=message,
        choices=choices,
        validate=lambda result: len(result) >= 1,
        invalid_message="should be at least 1 selection",
        instruction="(select at least 1)",
    ).execute()

    return selection
