#!/usr/bin/python3
"""Base Model that defines all common attributes/methods for other classes."""
import uuid
import datetime
import models


class BaseModel:
    """Base class for models with basic methods."""

    def __init__(self, *args, **kwargs):
        """Init a new instance with ids, timestamps, and optional attrs."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    date_format = "%Y-%m-%dT%H:%M:%S.%f"
                    setattr(self, key,
                            datetime.datetime.strptime(value, date_format))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            models.storage.new(self)

    def __str__(self):
        """Return a string repr: '[ClassName] (id) attributes'."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """Update 'updated_at' timestamp and saves using a storage model."""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """Convert attrs to a dict, incl. class info and timestamps."""
        dict_result = self.__dict__.copy()
        dict_result.update(
            {
                "__class__": self.__class__.__name__,
                "created_at": self.created_at.isoformat(),
                "updated_at": self.updated_at.isoformat(),
            }
        )
        return dict_result
