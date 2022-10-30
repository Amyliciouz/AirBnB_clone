#!/usr/bin/python3
""" contains unittest class for FileStorage"""
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os
import json
import unittest
from datetime import datetime
import models


class test_FileStorage(unittest.TestCase):
    """ unittest class to test FileStorage instantiation """

    def test_storage_init(self):
        self.assertEqual(type(models.storage), FileStorage)

    def test_FileStorage_init_with_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)


class TestFileStorage_methods(unittest.TestCase):
    """Unittests for methods in FileStorage class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}


if __name__ == "__main__":
    unittest.main()
