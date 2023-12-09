#!/usr/bin/python3
"""File Storage Model for managing the app storage."""
import json
import os
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """Handles storage of objects in a JSON file."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns a dictionary of all stored objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to the storage."""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects.update({key: obj})

    def save(self):
        """Serializes and saves all objects to the JSON file."""
        serialized_objects = {}
        for obj_id, obj in FileStorage.__objects.items():
            serialized_objects[obj_id] = obj.to_dict()
        with open(FileStorage.__file_path, "w") as json_file:
            json.dump(serialized_objects, json_file)

    def reload(self):
        """Loads objects from the JSON file into the storage."""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as json_file:
                loaded_data = json.load(json_file)
                for obj_id, obj_dict in loaded_data.items():
                    cls_name = obj_dict["__class__"]
                    FileStorage.__objects[obj_id] = eval(cls_name)(**obj_dict)
