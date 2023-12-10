#!/usr/bin/python3
"""Defines unittests for models/state.py.

Unittest classes:
    TestState
"""
import unittest
import models
from models.state import State


class TestState(unittest.TestCase):
    def test_init(self):
        """Test the initialization of State instances."""
        state1 = State()
        self.assertEqual(State, type(State()))
        self.assertNotEqual(state1.id, State().id)
        self.assertIsInstance(state1, State)

    def test_new_instance(self):
        """Test the creation of a new State instance and its storage."""
        self.assertIn(State(), models.storage.all().values())

    def test_name(self):
        """Test the name attribute of State instances."""
        state1 = State()
        self.assertEqual(str, type(state1.name))
        self.assertTrue(hasattr(state1, "name"))


if __name__ == "__main__":
    unittest.main()
