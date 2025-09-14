#!/usr/bin/python3
"""
Serializes instances to a JSON file and deserializes JSON file to instances.
"""
import json
from models.base_model import BaseModel


class FileStorage():
    """
    Serializes and deserializes objects to/from a JSON file.
    """
    __file_path = "file.json"
    __objects = {}
    imported_classes = {
        "BaseModel": BaseModel
    }

    def all(self):
        """Returns dictionary representation of all objects"""
        return self.__objects

    def new(self, obj):
        """Adds new object to objects using the key <class name>.<id>"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Saves __objects to file __file_path in JSON format"""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Loads the JSON file back into __objects"""
        try:
            with open(self.__file_path, "r") as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split(".")
                    if class_name in self.imported_classes:
                        obj_instance = self.imported_classes[class_name](
                            **value)
                        self.__objects[key] = obj_instance

        except FileNotFoundError:
            pass
