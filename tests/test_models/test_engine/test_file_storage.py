#!/usr/bin/python3
"""Test module for the FileStorage class."""
import unittest
import os
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class Test_FileStorage(unittest.TestCase):
    """Test class for the FileStorage class."""

    # Test if FileStorage instance is created
    def test__FileStorage(self):
        """Test if FileStorage instance is created."""
        self.assertEqual(type(FileStorage()), FileStorage)

    # Test if TypeError is raised when an argument is passed to FileStorage
    def test__FileStorage_with_arg(self):
        """Test if TypeError is raised when an argument is passed to
        FileStorage."""
        self.assertRaises(TypeError)

    # Test if the file_path attribute is a string
    def test__FileStorage_str_filepath(self):
        """Test if the file_path attribute is a string."""
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    # Test if the objects attribute is a dictionary
    def test__FileStorage_object(self):
        """Test if the objects attribute is a dictionary."""
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    # Test if models.storage is an instance of FileStorage
    def test__Storage_init(self):
        """Test if models.storage is an instance of FileStorage."""
        self.assertEqual(type(models.storage), FileStorage)

    @classmethod
    def setUp(self):
        """Set up for the tests."""
        try:
            os.rename("file.json", "tmp")
        except FileNotFoundError:
            pass

    @classmethod
    def tearDown(self):
        """Clean up after the tests."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp", "file.json")
        except FileNotFoundError:
            pass
        FileStorage._FileStorage_objects = {}

    # Test if all method returns a dictionary
    def test_all(self):
        """Test if all method returns a dictionary."""
        self.assertEqual(dict, type(models.storage.all()))

    # Test if TypeError is raised when an argument is passed to all method
    def test_all_arg(self):
        """Test if TypeError is raised when an argument is passed
        to all method."""
        with self.assertRaises(TypeError):
            models.storage.all(None)

    # Test if new method adds instances to the storage
    # and checks if they are saved
    def test_new(self):
        """Test if new method adds instances to the storage and
        checks if they are saved."""
        Based_model_obj = BaseModel()
        User_Obj = User()
        State_Obj = State()
        Place_Obj = Place()
        City_Obj = City()
        Amenity_Obj = Amenity()
        Review_Obj = Review()

        models.storage.new(Based_model_obj)
        models.storage.new(User_Obj)
        models.storage.new(State_Obj)
        models.storage.new(Place_Obj)
        models.storage.new(City_Obj)
        models.storage.new(Amenity_Obj)
        models.storage.new(Review_Obj)

        # Check if the instances are added to the storage
        self.assertIn("BaseModel." + Based_model_obj.id,
                      models.storage.all().keys())
        self.assertIn(Based_model_obj, models.storage.all().values())
        self.assertIn("User." + User_Obj.id, models.storage.all().keys())
        self.assertIn(User_Obj, models.storage.all().values())
        self.assertIn("State." + State_Obj.id, models.storage.all().keys())
        self.assertIn(State_Obj, models.storage.all().values())
        self.assertIn("Place." + Place_Obj.id, models.storage.all().keys())
        self.assertIn(Place_Obj, models.storage.all().values())
        self.assertIn("City." + City_Obj.id, models.storage.all().keys())
        self.assertIn(City_Obj, models.storage.all().values())
        self.assertIn("Amenity." + Amenity_Obj.id, models.storage.all().keys())
        self.assertIn(Amenity_Obj, models.storage.all().values())
        self.assertIn("Review." + Review_Obj.id, models.storage.all().keys())
        self.assertIn(Review_Obj, models.storage.all().values())

    def test_new_args(self):
        """Test if TypeError is raised when an argument is passed
        to new method."""
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_save(self):
        """Test if instances are saved in the file."""
        # Create instances of the models
        base_model = BaseModel()
        user = User()
        state = State()
        place = Place()
        city = City()
        amenity = Amenity()
        review = Review()

        # Add the instances to the storage and save
        models.storage.new(base_model)
        models.storage.new(user)
        models.storage.new(state)
        models.storage.new(place)
        models.storage.new(city)
        models.storage.new(amenity)
        models.storage.new(review)
        models.storage.save()

        # Check if the instances are saved in the file
        save_text = ""
        with open("file.json", "r") as file:
            save_text = file.read()
            self.assertIn("BaseModel." + base_model.id, save_text)
            self.assertIn("User." + user.id, save_text)
            self.assertIn("State." + state.id, save_text)
            self.assertIn("Place." + place.id, save_text)
            self.assertIn("City." + city.id, save_text)
            self.assertIn("Amenity." + amenity.id, save_text)
            self.assertIn("Review." + review.id, save_text)

    # Test if TypeError is raised when an argument is passed to save
    def test_save_arg(self):
        """Test if TypeError is raised when an argument is passed to save."""
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        """Test if instances are reloaded in the storage."""
        # Create instances of the models
        base_model = BaseModel()
        user = User()
        state = State()
        place = Place()
        city = City()
        amenity = Amenity()
        review = Review()

        # Add the instances to the storage and save
        models.storage.new(base_model)
        models.storage.new(user)
        models.storage.new(state)
        models.storage.new(place)
        models.storage.new(city)
        models.storage.new(amenity)
        models.storage.new(review)
        models.storage.save()
        models.storage.reload()

        # Check if the instances are reloaded in the storage
        objects = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + base_model.id, objects)
        self.assertIn("User." + user.id, objects)
        self.assertIn("State." + state.id, objects)
        self.assertIn("Place." + place.id, objects)
        self.assertIn("City." + city.id, objects)
        self.assertIn("Amenity." + amenity.id, objects)
        self.assertIn("Review." + review.id, objects)

    def test_reload_with_arg(self):
        """Test if TypeError is raised when an argument is passed to reload."""
        # Test if TypeError is raised when an argument is passed to reload
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
