#!/usr/bin/python3
"""Unittest module for the Amenity Class."""

import unittest
from datetime import datetime
import time
from models.amenity import Amenity
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel

class TestAmenity(unittest.TestCase):
    def test_inheritance(self):
        """Test inherits from BaseModel"""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_attributes(self):
        """Test attributes of Amenity class"""
        amenity = Amenity()

        # Test if name attribute exists
        self.assertTrue(hasattr(amenity, 'name'))

        # Test if name attribute is an empty string
        self.assertEqual(amenity.name, "")

    def test_str_representation(self):
        """Test string representation of Amenity object"""
        amenity = Amenity()
        expected_str = f"[Amenity] ({amenity.id}) {amenity.__dict__}"
        self.assertEqual(str(amenity), expected_str)

    def test_save_method(self):
        """Test save method of Amenity"""
        amenity = Amenity()
        old_updated_at = amenity.updated_at

        amenity.save()

        self.assertNotEqual(amenity.updated_at, old_updated_at)

if __name__ == '__main__':
    unittest.main()
