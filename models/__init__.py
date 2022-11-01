#!/usr/bin/python3
""" unique FileStorage instance for app"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
