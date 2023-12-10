#!/usr/bin/python3
"""Defines unittests for models/city.py.

Unittest classes:
    TestCity
"""
import unittest
import models
from models.city import City


class TestCity(unittest.TestCase):
    def test_init(self):
        """Test the initialization of City instances."""
        city1 = City()
        city2 = City()
        self.assertEqual(City, type(City()))
        self.assertNotEqual(city1.id, city2.id)
        self.assertIsInstance(city1, City)

    def test_new_instance(self):
        """Test the creation of a new City instance and its storage."""
        self.assertIn(City(), models.storage.all().values())

    def test_state_id(self):
        """Test the state_id attribute of City instances."""
        city1 = City()
        self.assertEqual(str, type(city1.state_id))
        self.assertTrue(hasattr(city1, "state_id"))

    def test_name(self):
        """Test the name attribute of City instances."""
        city1 = City()
        self.assertEqual(str, type(city1.name))
        self.assertTrue(hasattr(city1, "name"))


if __name__ == "__main__":
    unittest.main()
