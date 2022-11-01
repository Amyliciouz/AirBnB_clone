#!/usr/bin/python3
""" this module contains Review class that
inherits from the BaseModel class."""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class definition"""
    place_id = ""
    user_id = ""
    text = ""
