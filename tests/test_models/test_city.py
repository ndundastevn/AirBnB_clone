#!/usr/bin/python3
"""Unittest module for the City Class."""

import unittest
from datetime import datetime
import time
from models.city import City
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    def test_inheritance(self):
        """Test if City class inherits from parent class BaseModel"""
        self.assertTrue(issubclass(City, BaseModel))

    def test_attributes(self):
        """Test attributes of City class"""
        city = City()

        # Test if state_id attribute exists
        self.assertTrue(hasattr(city, 'state_id'))

        # Test if name attribute exists
        self.assertTrue(hasattr(city, 'name'))

        # Test if state_id attribute is an empty string
        self.assertEqual(city.state_id, "")

        # Test if name attribute is an empty string
        self.assertEqual(city.name, "")

    def test_str_representation(self):
        """Test string representation of City object"""
        city = City()
        expected_str = f"[City] ({city.id}) {city.__dict__}"
        self.assertEqual(str(city), expected_str)

    def test_save_method(self):
        """Test save method of City"""
        city = City()
        old_updated_at = city.updated_at

        city.save()

        self.assertNotEqual(city.updated_at, old_updated_at)

if __name__ == '__main__':
    unittest.main()
