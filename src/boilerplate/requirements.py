"""This File contains all the methods required to capture user preferences to setup the project"""

from pathlib import Path


def get_location(message: str) -> Path:
    """Method to get `File` or `Folder` location from the user as Path

    Args:
        message (str): Message to show to the user

    Returns:
        Path: Path provided by the end-user as `Path`
    """
    return Path(input(message))


def get_input(message: str) -> str:
    """Method to get User Input from the User as String

    Args:
        message (str): Message to show to the user

    Returns:
        str: Input provided by the end-user as `string`
    """
    return str(input(message))


def get_confirmation(message: str, selection: bool = False) -> bool:
    """Method to get confirmation on against the displayed message

    Args:
        message (str): Message to show to the user
        selection (bool): User Preference agains

    Returns:
        bool: Final preference by user against the displayed message
    """
    if not selection:
        user_input = str(input(message))
        if "y" in user_input.lower():
            selection = True
    return selection
