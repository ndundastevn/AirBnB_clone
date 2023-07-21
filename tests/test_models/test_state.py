#!/usr/bin/python3
"""Unittest for state class"""

import unittest
from datetime import datetime
import time
from models.state import State
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """TestState clase for the State class."""

    def setUp(self):
        """Sets up tests"""
        pass

    def tearDown(self):
        """Tears down test methods of teststate class."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets FileStorage"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instantiation(self):
        """Tests instantiation"""
        bb = State()
        self.assertEqual(str(type(bb)), "<class 'models.state.State'>")
        self.assertIsInstance(bb, State)
        self.assertTrue(issubclass(type(bb), BaseModel))

    def test_8_attributes(self):
        """Tests the attributes of"""
        attributes = storage.attributes()["State"]
        oo = State()
        for kk, vv in attributes.items():
            self.assertTrue(hasattr(oo, kk))
            self.assertEqual(type(getattr(oo, kk, None)), vv)

if __name__ == "__main__":
    unittest.main()
