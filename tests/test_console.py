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
    def test_EOF_exits(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("EOF"))

    def test_count_State(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.count()"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.count()"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.count()"))
            self.assertEqual("1", output.getvalue().strip())

if __name__ == "__main__":
    unittest.main()
