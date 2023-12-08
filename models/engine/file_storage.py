#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects.update({key: obj})

    def save(self):
        serialized_objects = {}
        for obj_id, obj in FileStorage.__objects.items():
            serialized_objects[obj_id] = obj.to_dict()
        with open(FileStorage.__file_path, "w") as json_file:
            json.dump(serialized_objects, json_file, indent=4)

    # def reload(self):
    #     if os.path.exists(FileStorage.__file_path):
    #         with open(FileStorage.__file_path, "r") as json_file:
    #             loaded_data = json.load(json_file)
    #             for obj_id, obj_dict in loaded_data.items():
    #                 class_name = obj_dict["__class__"]
    #                 FileStorage.__objects[obj_id] = eval(class_name)(**obj_dict)

    def reload(self):
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as json_file:
                loaded_data = json.load(json_file)
                for obj_id, obj_dict in loaded_data.items():
                    FileStorage.__objects[obj_id] = BaseModel(**obj_dict)
