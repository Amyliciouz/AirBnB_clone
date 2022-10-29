#!/usr/bin/python3
import uuid
import datetime

"""The Base Model:contains instances and methods
for other classes"""


class BaseModel:
    """ class definition """

    def __init__(self):
        """ class instantiation"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """prints [<class name>] (<self.id>) <self.__dict__>"""
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                self.id, self.__dict__))

    def save(self):
        """ updates updated_at attribute"""
        self.updated_at = datetime.now()
        return self.updated_at

    def to_dict(self):
        """returns a dict containing all key,value of dict"""
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy
