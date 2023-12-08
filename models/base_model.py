#!/usr/bin/python3
"""Base Model that defines all common attributes/methods for other classes"""

import uuid
import datetime
from . import storage


class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    date_format = "%Y-%m-%dT%H:%M:%S.%f"
                    setattr(self, key, datetime.datetime.strptime(value, date_format))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            storage.new(self)

    def __str__(self):
        return "[{}] ({}) {}".format(__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        dict_result = self.__dict__.copy()
        dict_result.update(
            {
                "__class__": __class__.__name__,
                "created_at": self.created_at.isoformat(),
                "updated_at": self.updated_at.isoformat(),
            }
        )
        return dict_result
