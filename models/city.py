#!/usr/bin/python3

from models.base_model import BaseModel


class City(BaseModel):
    """ city class for the Air_bnb project
    Attributes:
        name (str): name of the city
    """
    state_id = ""
    name = ""
