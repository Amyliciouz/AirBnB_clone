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
