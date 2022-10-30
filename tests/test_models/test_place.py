#!/usr/bin/python3
"""Unittest Place"""
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import unittest


class test_place(unittest.TestCase):
    """
    Unittests for the Place class.
    """
    def test_class(self):
        """
        Tests if class is named correctly.
        """
        place1 = Place()
        self.assertEqual(place1.__class__.__name__, "Place")

    def test_superclass(self):
        """
        Tests if Class inherits from BaseModel.
        """
        place1 = Place()
        self.assertTrue(issubclass(place1.__class__, BaseModel))
