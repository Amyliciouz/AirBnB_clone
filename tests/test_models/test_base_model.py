#!/usr/bin/python3
""" Unittest Module for base_model class"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """unittest class of BaseModel, inheriting from unittest module"""
    def test_created_at(self):
        """tests that created_at is a datetime value"""
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_update_at(self):
        """checks that updated_at is a datetime value"""
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_id(self):
        """checks that id is a string"""
        self.assertEqual(str, type(BaseModel().id))

    def test_uuid(self):
        """checks that every id is unique"""
        id_1 = BaseModel()
        id_2 = BaseModel()
        self.assertNotEqual(id_1.id, id_2.id)

    def test_to_dict_type(self):
        """checks that to_dict returns a dict"""
        new_dict = BaseModel().to_dict()
        self.assertEqual(dict, type(new_dict))

    def test_to_dict_attr(self):
        """checks that to_dict includes keys and values of
        new public attributes added to the BaseModel class"""
        cls = BaseModel()
        cls.nickname = "Watcher"
        cls.code = "rU3y"
        self.assertIn("nickname", cls.to_dict())
        self.assertIn("code", cls.to_dict())


if __name__ == '__main__':
    unittest.main()
