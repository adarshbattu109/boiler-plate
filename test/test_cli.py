"""Class to test the `CLI` module and associated functions
"""
import unittest
from unittest import mock
from pathlib import Path
from boilerplate.cli import get_input, get_location, get_confirmation, get_selection_from_choices, get_multi_select_choices

available_choices = [
    "Apple",
    "Cherry",
    "Orange",
    "Peach",
    "Melon",
    "Strawberry",
    "Grapes",
]


class TestCLI(unittest.TestCase):
    """Class containing tests for CLI funtions"""

    def test_get_input(self) -> None:
        """Method to test get_location method"""
        with mock.patch("builtins.input", lambda _: "Neo"):
            expected = "Neo"
            actual = get_input("Enter your name")
            assert actual == expected

    def test_get_location(self) -> None:
        """Method to test get_location method"""
        with mock.patch("builtins.input", lambda _: "."):
            user_path = get_location("Enter a directory location : ")
            assert Path == type(user_path)

    def test_get_confirmation(self) -> None:
        """Method to test get_confirmation method"""
        with mock.patch("builtins.input", lambda _: "y"):
            confirm = get_confirmation("Take the red Pill 💊 ?")
            assert bool == type(confirm)
            assert confirm is True

    def test_get_selection_from_choices(self) -> None:
        """Method to test get_selection_from_choices method"""
        with mock.patch("builtins.input", lambda _: " "):
            select = get_selection_from_choices("Select one fruit", available_choices)
            assert str == type(select)
            assert "Apple" == select

    def test_get_multi_select_choices(self) -> None:
        """Method to test get_multi_select_choices method"""
        with mock.patch("builtins.input", lambda _: "  "):
            multi_select = get_multi_select_choices("Select fruits", available_choices)
            assert list == type(multi_select)
            assert ["Apple", "Cherry"] == multi_select


if __name__ == "__main__":
    unittest.main()
