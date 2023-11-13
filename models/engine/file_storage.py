#!/usr/bin/python3
"""
It contains FileStorage class model
- class model

"""
import json

from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity


class FileStorage:
    """
    The instances - JSON file and
    deserializes JSON file - instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        It returns dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        It sets in __objects `obj` with key <obj class name>.id
        """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """
        It serialize __objects - JSON file
        """
        with open(self.__file_path, mode="w") as f:
            dict_storage = {}
            for j, x in self.__objects.items():
                dict_storage[j] = x.to_dict()
            json.dump(dict_storage, f)

    def reload(self):
        """
        Its a JSON file to __objects
        -> Only IF it does exists!
        """
        try:
            with open(self.__file_path, encoding="utf-8") as f:
                for obj in json.load(f).values():
                    self.new(eval(obj["__class__"])(**obj))
        except FileNotFoundError:
            return
