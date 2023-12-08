#!/usr/bin/python3
import json
import os


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + "." + obj.id
        value = obj.to_dict()
        FileStorage.__objects.update({key: value})

    def save(self):
        updated_objects = {}
        for obj in FileStorage.__objects.keys():
            updated_objects[obj] = FileStorage.__objects[obj].to_dict()
        FileStorage.__objects = updated_objects.copy()
        with open(FileStorage.__file_path, "w") as json_file:
            json.dump(FileStorage.__objects, json_file, indent=4)

    def reload(self):
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as json_file:
                FileStorage.__objects = json.load(json_file)
