"""Class to test the `CLI` module and associated functions
"""
import unittest

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

    def test_get_input(self):
        """Method to test get_location method"""
        user_input = get_input("Enter your name : ")
        assert str == type(user_input)
        assert "Neo" == user_input

    def test_get_location(self):
        """Method to test get_location method"""
        user_path = get_location("Enter a directory location : ")
        assert Path == type(user_path)

    def test_get_confirmation(self):
        """Method to test get_confirmation method"""
        confirm = get_confirmation("Take the red Pill 💊 ?")
        assert bool == type(confirm)
        assert confirm is True

    def test_get_selection_from_choices(self):
        """Method to test get_selection_from_choices method"""
        select = get_selection_from_choices("Select one fruit", available_choices)
        assert str == type(select)
        assert "Apple" == select

    def test_get_multi_select_choices(self):
        """Method to test get_multi_select_choices method"""
        multi_select = get_multi_select_choices("Select fruits", available_choices)
        assert list == type(multi_select)
        assert ["Apple", "Cherry"] == multi_select


if __name__ == "__main__":
    unittest.main()
