#!/usr/bin/python3
"""Unittest State"""
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import unittest 


class test_state(unittest.TestCase):
    """
    Unittests for the State class.
    """

    def test_class(self):
        """
        Tests if class is named correctly.
        """
        state1 = State()
        self.assertEqual(state1.__class__.__name__, "State")

    def test_superclass(self):
        """
        Tests if Class inherits from BaseModel.
        """
        state1 = State()
        self.assertEqual(state1.__class__.__name__, "State")
