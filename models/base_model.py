#!/usr/bin/python3
import models
import uuid
from datetime import datetime

"""The Base Model:contains instances and methods
for other classes"""


class BaseModel:
    """ class definition """

    def __init__(self, *args, **kwargs):
        """ class instantiation using args and kwargs"""
        if kwargs is not None:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key == "__class__":
                    continue
                setattr(self, key, value)
            else:
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
