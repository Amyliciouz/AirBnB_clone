#!/usr/bin/python3
""" This model contains FileStorage class"""
from models.base_model import BaseModel
import json
from os import path
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dict __objects"""
        return self.__objects

    def new(self, obj):
        """ sets obj_class.id as key for objects
        in __objects dict"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to a json file """
        dict_obj = {}
        for value, key in self.__objects.items():
            dict_obj[key] = value.to_dict()
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            f.write(json.dumps(json_dict))

    def reload(self):
        """ deserializes json file to __objects"""
        if path.exists(self.__file_path):
            with open(self.__file_path, mode='r', encoding='utf-8') as f:
                json_dict = json.loads(f.read())
                for key, value in json_dict.items():
                    self.__objects[key] = eval(value['__class__'])(**value)
