#!/usr/bin/python3
"""Defines unittests for console.py.

Unittest classes:
    TestHBNBCommand_prompting

"""

import unittest
from models import storage
from unittest.mock import patch
from models.engine.file_storage import FileStorage
from console import HBNBCommand


class TestHBNBCommand_prompting(unittest.TestCase):
    """Unittests for testing prompting of the HBNB command interpreter."""

    def test_console_prompt(self):
        """Test the prompt attribute of the HBNB command interpreter."""
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_function_quit(self):
        """Test the do_quit method of the HBNB command interpreter."""
        hbnb_command_instance = HBNBCommand()
        self.assertTrue(hbnb_command_instance.do_quit(None))


if __name__ == "__main__":
    unittest.main()
