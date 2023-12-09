#!/usr/bin/python3
"""Test BaseModel module using unittest"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class Test_Base_Model_init(unittest.TestCase):
    """Test cases for the initialization of the BaseModel class."""

    def test__init(self):
        """Test the initialization of BaseModel instances."""
        my_model = BaseModel()
        self.assertEqual(str, type(my_model.id))
        self.assertEqual(datetime, type(my_model.created_at))
        self.assertEqual(datetime, type(my_model.updated_at))

    def test__save(self):
        """Test the save method of BaseModel instances."""
        my_model = BaseModel()
        initial_updated_at = my_model.updated_at
        my_model.save()
        current_updated_at = my_model.updated_at
        self.assertNotEqual(initial_updated_at, current_updated_at)

    def test_to_dic(self):
        """Test the to_dict method of BaseModel instances."""
        my_model = BaseModel()
        model_dic = my_model.to_dict()
        self.assertIsInstance(model_dic, dict)
        self.assertEqual(model_dic["__class__"], my_model.__class__.__name__)
        self.assertEqual(model_dic["id"], my_model.id)
        self.assertEqual(model_dic["created_at"],
                         my_model.created_at.isoformat())
        self.assertEqual(model_dic["updated_at"],
                         my_model.updated_at.isoformat())

    def test_str_method(self):
        """Test the string representation of BaseModel instances."""
        my_model = BaseModel()
        self.assertTrue(str(my_model).startswith("[BaseModel]"))
        self.assertIn(my_model.id, str(my_model))
        self.assertIn(str(my_model.__dict__), str(my_model))


if __name__ == "__main__":
    unittest.main()
