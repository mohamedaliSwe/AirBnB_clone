#!/usr/bin/python3
"""
Defines the base model for the AirBNB_clone project
"""
import uuid
from datetime import datetime
import models


class BaseModel():
    """"
    Defines all common attributes and methods for the classes.

    Attributes:
        id (str): Unique identifier for each instance of BaseModel.
        created_at (datetime): The datetime when the intance is created.
        updated_at (datetime): The datetime when the instance is modified.
    """

    def __init__(self, *args, **kwargs):
        """Initializes a new instance of BaseModel"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')

                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Returns string representation of an instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates updated_at attribute with the current date and time"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dict of all keys/values of __dict__ of the instance"""
        object_dict = self.__dict__.copy()
        object_dict["__class__"] = self.__class__.__name__
        object_dict["created_at"] = self.created_at.isoformat()
        object_dict["updated_at"] = self.updated_at.isoformat()
        return object_dict
