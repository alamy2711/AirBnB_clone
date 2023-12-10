#!/usr/bin/python3
"""Defines unittests for models/review.py.

Unittest classes:
    TestReview
"""

import models
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    def test_init(self):
        """Test the initialization of Review instances."""
        review1 = Review()
        review2 = Review()
        self.assertEqual(Review, type(Review()))
        self.assertNotEqual(review1.id, review2.id)
        self.assertIsInstance(review1, Review)

    def test_new_instance(self):
        """Test the creation of a new Review instance and its storage."""
        self.assertIn(Review(), models.storage.all().values())

    def test_place_id(self):
        """Test the place_id attribute of Review instances."""
        review1 = Review()
        self.assertEqual(str, type(review1.place_id))
        self.assertTrue(hasattr(review1, "place_id"))

    def test_user_id(self):
        """Test the user_id attribute of Review instances."""
        review1 = Review()
        self.assertEqual(str, type(review1.user_id))
        self.assertTrue(hasattr(review1, "user_id"))

    def test_text(self):
        """Test the text attribute of Review instances."""
        review1 = Review()
        self.assertEqual(str, type(review1.text))
        self.assertTrue(hasattr(review1, "text"))


if __name__ == "__main__":
    unittest.main()
