#!/usr/bin/python3
"""This module contains City class
that inherits from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """ City class defintion"""
    state_id = ""
    name = ""
