#!/usr/bin/python3
"""Unittest for Amenity"""
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import unittest


class test_amenity(unittest.TestCase):
    """
    unit test for amenity class
    """

    def test_class(self):
        """
        Tests if the class is named correctly.
        """
        amenity1 = Amenity()
        self.assertEqual(amenity1.__class__.__name__, "Amenity")

    def test_superclass(self):
        """
        Tests if class inherits from BaseModel.
        """
        amenity1 = Amenity()
        self.assertTrue(issubclass(amenity1.__class__, BaseModel))
