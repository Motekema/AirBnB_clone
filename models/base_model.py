#!/usr/bin/python3
"""
Module that applys BaseModel class
"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    Its class defines common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        It initialize BaseModel class
        """

        from models import storage
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)
        else:
            for keys, value in kwargs.items():
                if keys != '__class__':
                    if keys in ('created_at', 'updated_at'):
                        setattr(self, keys, datetime.fromisoformat(value))
                    else:
                        setattr(self, keys, value)

    def __str__(self):
        """
        It returns string representation of BaseModel object.
        [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)

    def save(self):
        """
        It updates 'self.updated_at' with current datetime
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        It returns dictionary containing all keys/values of __dict__
        of instance:
        - Instance attributes set will returned
        - keys __class__ is added with class name of object
        - It created_at- updated_at must converted string object in ISO
        object
        """
        dict_1 = self.__dict__.copy()
        dict_1["__class__"] = self.__class__.__name__
        for x, j in self.__dict__.items():
            if x in ("created_at", "updated_at"):
                j = self.__dict__[x].isoformat()
                dict_1[x] = j
        return dict_1
