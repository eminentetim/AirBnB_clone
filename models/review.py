#!/usr/bin/python3
""" Module for the Review class of tha Air_bnb project """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class for the Air_bnb project
    Attributes:
        name (str): name of the review
    """
    place_id = ""
    user_id = ""
    text = ""
