#!/usr/bin/python3
"""Defines unittests for models/user.py.

Unittest classes:
    TestUserInstantiation
    TestUserSave
    TestUserToDict
"""
import unittest
import models
from models.user import User


class TestUser(unittest.TestCase):
    def test_init(self):
        """Test the initialization of User instances."""
        user1 = User()
        user2 = User()
        self.assertEqual(User, type(User()))
        self.assertNotEqual(user1.id, user2.id)
        self.assertIsInstance(user1, User)

    def test_new_instance(self):
        """Test the creation of a new User instance and its storage."""
        self.assertIn(User(), models.storage.all().values())

    def test_email(self):
        """Test the email attribute of User instances."""
        user1 = User()
        self.assertEqual(str, type(user1.email))
        self.assertTrue(hasattr(user1, "email"))

    def test_password(self):
        """Test the password attribute of User instances."""
        user1 = User()
        self.assertEqual(str, type(user1.password))
        self.assertTrue(hasattr(user1, "password"))

    def test_id(self):
        """Test the id attribute of User instances."""
        user1 = User()
        self.assertEqual(str, type(user1.id))
        self.assertTrue(hasattr(user1, "id"))

    def test_first_name(self):
        """Test the first_name attribute of User instances."""
        user1 = User()
        self.assertEqual(str, type(user1.first_name))
        self.assertTrue(hasattr(user1, "first_name"))

    def test_last_name(self):
        """Test the last_name attribute of User instances."""
        user1 = User()
        self.assertEqual(str, type(user1.last_name))
        self.assertTrue(hasattr(user1, "last_name"))


if __name__ == "__main__":
    unittest.main()
