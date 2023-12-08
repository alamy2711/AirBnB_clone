#!/usr/bin/python3
"""
"""

import unittest
from datetime import datetime
from models.base_model import BaseModel

class Test_Base_Model_init(unittest.TestCase):
    """
    """
    
    def test__init(self):
        my_model = BaseModel()

        self.assertEqual(str, type(BaseModel().id))
        self.assertEqual(datetime, type(BaseModel().created_at))
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test__save(self):
        my_model = BaseModel()

        initial_updated_at = my_model.updated_at
        my_model.save()
        current_updated_at = my_model.updated_at
        
        self.assertNotEqual(initial_updated_at, current_updated_at)
    
    def test_to_dic(self):
        my_model = BaseModel()

        model_dic = my_model.to_dict()
        self.assertIsInstance(model_dic, dict)

        self.assertEqual(model_dic["__class__"], my_model.__class__.__name__)
        self.assertEqual(model_dic["id"], my_model.id)
        self.assertEqual(model_dic["created_at"], my_model.created_at.isoformat())
        self.assertEqual(model_dic["updated_at"], my_model.updated_at.isoformat())


    def test_str_method(self):
        my_model = BaseModel()

        self.assertTrue(str(my_model).startswith('[BaseModel]'))
        self.assertIn(my_model.id, str(my_model))
        self.assertIn(str(my_model.__dict__),str(my_model))

if __name__ == "__main__":
    unittest.main()
