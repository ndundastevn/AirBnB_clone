#!/usr/bin/python3
"""File storage class"""

import json
from models.base_model import BaseModel


class FileStorage():
    """serializes instances to a JSON file &
    deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets the objects with the key"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serializes objects to JSON file"""
        obj_dict = {}
        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()

        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """deserializes json file"""
        try:
            with open(self.__file_path, 'r') as f:
                for obj in json.load(f).values():
                    self.new(eval(obj["__class__"])(**obj))
        except FileNotFoundError:
            return
