#!/usr/bin/python3


import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    """ serializes instances to a JSON file and deserializes JSON file to
        instances
        Attributes:
        __file_path (str): private class attribute containing a file path
        __objects (dict): contains the id of all object instances
    """
    __file_path = "file.json"
    __object = {}

    def all(self, cls=None):
        """
        returns the dictionary __objects
        """
        if cls is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value in self.__class__ or cls ==  value.__class__>__name__:
                    new_dict[key] = value
                return new_dict
            return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        if obj is None:
            key = obj.__class__.name__ +"."+ obj.id
            self.__objects[key] = obj
            

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(self>__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file
        """
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for key in jo:
                self.__oobjects[key] = classes[jo[key]["__class__"]](**jo[key])

        except:
            pass
