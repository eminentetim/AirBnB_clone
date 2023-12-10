#!/usr/bin/python3
'''
All the imported models
'''

import uuid
from datetime import datetime


class BaseModel:
    """
    Attributes:
    id (str): id of an instance of this class
    created_at (datetime): time an imstance was created
    updated_at (datetime): time an instance of this object is updated
    Defining a base class
    """
    def __init__(self, *args, **kwargs):
        """ Creating a public instance attributes
         Initalizes an object of class Basemodel
        Args:
            args (tuple): variable lenght argument
            kwargs (dict): contains instance attributes and values
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.fromisoformat(value)
                elif key == "updated_at":
                    self.updated_at = datetime.fromisoformat(value)
                elif key == "__class__":
                    continue
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Implementing a method to print string"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """Updating the updated_at attributes with the current date time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Converting the instance attributes to a dictionary"""
        my_dict = dict(self.__dict__)
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict
