#!/usr/bin/python3

import uuid
from datetime import datetime as dt


class BaseModel():
    """
    Defining a base class
    """
    def __init__(self):
        """ Creating a public instance attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = dt.now()
        self.updated_at = dt.now()

    def __str__(self):
        """Implementing a method to print string"""
        return f"([{self.__class__.__name__}] ({self.id}) {self.__dict__})"

    def save(self):
        """Updating the updated_at attributes with the current date time"""
        self.updated_at = dt.now()

    def to_dict(self):
        """Converting the instance attributes to a dictionary"""
        my_dict = dict(self.__dict__)
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict
