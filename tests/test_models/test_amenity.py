#!/usr/bin/python3
"""Defines unittests for models/amenity.py.

Unittest classes:
    TestAmenity
"""
import unittest
import models
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def test_init(self):
        """Test the initialization of Amenity instances."""
        amenity1 = Amenity()
        self.assertEqual(Amenity, type(Amenity()))
        self.assertNotEqual(amenity1.id, Amenity().id)
        self.assertIsInstance(amenity1, Amenity)

    def test_new_instance(self):
        """Test the creation of a new Amenity instance and its storage."""
        self.assertIn(Amenity(), models.storage.all().values())

    def test_name(self):
        """Test the name attribute of Amenity instances."""
        amenity1 = Amenity()
        self.assertEqual(str, type(amenity1.name))
        self.assertTrue(hasattr(amenity1, "name"))


if __name__ == "__main__":
    unittest.main()
