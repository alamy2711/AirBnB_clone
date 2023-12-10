#!/usr/bin/python3
"""Defines unittests for models/place.py.

Unittest classes:
    TestPlace_instantiation
    TestPlace_save
    TestPlace_to_dict
"""
import os
import models
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    def test_init(self):
        """Test the initialization of Place instances."""
        place1 = Place()
        place2 = Place()
        self.assertEqual(Place, type(Place()))
        self.assertNotEqual(place1.id, place2.id)
        self.assertIsInstance(place1, Place)

    def test_new_instance(self):
        """Test the creation of a new Place instance and its storage."""
        self.assertIn(Place(), models.storage.all().values())

    def test_city_id(self):
        """Test the city_id attribute of Place instances."""
        place1 = Place()
        self.assertEqual(str, type(place1.city_id))
        self.assertTrue(hasattr(place1, "city_id"))

    def test_user_id(self):
        """Test the user_id attribute of Place instances."""
        place1 = Place()
        self.assertEqual(str, type(place1.user_id))
        self.assertTrue(hasattr(place1, "user_id"))

    def test_name(self):
        """Test the name attribute of Place instances."""
        place1 = Place()
        self.assertEqual(str, type(place1.name))
        self.assertTrue(hasattr(place1, "name"))

    def test_description(self):
        """Test the description attribute of Place instances."""
        place1 = Place()
        self.assertEqual(str, type(place1.description))
        self.assertTrue(hasattr(place1, "description"))

    def test_number_rooms(self):
        """Test the number_rooms attribute of Place instances."""
        place1 = Place()
        self.assertEqual(int, type(place1.number_rooms))
        self.assertTrue(hasattr(place1, "number_rooms"))

    def test_number_bathrooms(self):
        """Test the number_bathrooms attribute of Place instances."""
        place1 = Place()
        self.assertEqual(int, type(place1.number_bathrooms))
        self.assertTrue(hasattr(place1, "number_bathrooms"))

    def test_max_guest(self):
        """Test the max_guest attribute of Place instances."""
        place1 = Place()
        self.assertEqual(int, type(place1.max_guest))
        self.assertTrue(hasattr(place1, "max_guest"))

    def test_price_by_night(self):
        """Test the price_by_night attribute of Place instances."""
        place1 = Place()
        self.assertEqual(int, type(place1.price_by_night))
        self.assertTrue(hasattr(place1, "price_by_night"))

    def test_latitude(self):
        """Test the latitude attribute of Place instances."""
        place1 = Place()
        self.assertEqual(float, type(place1.latitude))
        self.assertTrue(hasattr(place1, "latitude"))

    def test_longitude(self):
        """Test the longitude attribute of Place instances."""
        place1 = Place()
        self.assertEqual(float, type(place1.longitude))
        self.assertTrue(hasattr(place1, "longitude"))

    def test_amenity_ids(self):
        """Test the amenity_ids attribute of Place instances."""
        place1 = Place()
        self.assertEqual(list, type(place1.amenity_ids))
        self.assertTrue(hasattr(place1, "amenity_ids"))


if __name__ == "__main__":
    unittest.main()
