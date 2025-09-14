#!/usr/bin/python3
"""
Defines the base model for the AirBNB_clone project
"""
import uuid
from datetime import datetime


class BaseModel():
    """"Defines all commont attributes and methods for the classes."""

    def __init__(self):
        """Initializes a new instance of BaseModel"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """Returns string representation of an instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates updated_at attribute with the current date and time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dict of all keys/values of __dict__ of the instance"""
        object_dict = self.__dict__.copy()
        object_dict["__class__"] = self.__class__.__name__
        object_dict["created_at"] = self.created_at.isoformat()
        object_dict["updated_at"] = self.updated_at.isoformat()
        return object_dict
