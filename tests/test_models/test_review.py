#!/usr/bin/python3
"""Unittest for Review"""
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import unittest


class test_review(unittest.TestCase):
    """
    Unittests for the Review class.
    """
    def test_class(self):
        """
        Tests if class is named correctly.
        """
        rev1 = Review()
        self.assertEqual(rev1.__class__.__name__, "Review")

    def test_superclass(self):
        """
        Tests if Class inherits from BaseModel.
        """
        rev1 = Review()
        self.assertTrue(issubclass(rev1.__class__, BaseModel))
