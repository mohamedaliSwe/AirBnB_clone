#!/usr/bin/python3
"""
Initializes the storage engine for the models package.
It creates a singleton instance of FileStorage responsible for
serializing and deserializing objects to/from a JSON file.

Upon import, it loads previously saved objects from the file.
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
