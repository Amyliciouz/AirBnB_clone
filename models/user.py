#!/usr/bin/python3
""" this module contains the User class
inherits from BaseModel class"""
from models.base_model import BaseModel


class User(BaseModel):
    """ class User defintion"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
