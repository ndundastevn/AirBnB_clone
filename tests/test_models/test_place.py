#!/usr/bin/python3
"""Unittest module for the Place Class."""

import unittest
from datetime import datetime
import time
from models.place import Place
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    def setUp(self):
        # Set up an instance of Place before each test
        self.place = Place()

    def tearDown(self):
        # tear down the instance of Place after each test begins
        del self.place

    def test_attributes_initialization(self):
        # Check attributes initializion
        self.assertEqual(self.place.city_id, "") 
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)  # Zero
        self.assertEqual(self.place.number_bathrooms, 0)  # Zero
        self.assertEqual(self.place.max_guest, 0)  # Zero
        self.assertEqual(self.place.price_by_night, 0)  # Zero
        self.assertEqual(self.place.latitude, 0.0)  
        self.assertEqual(self.place.longitude, 0.0)  
        self.assertEqual(self.place.amenity_ids, []) 

    def test_attributes_assignment(self):
        # Assign values and check if they are assigned correctly
        self.place.city_id = "1234"
        self.place.user_id = "4567"
        self.place.name = "Sample Place"
        self.place.description = "This is a sample place"
        self.place.number_rooms = 33
        self.place.number_bathrooms = 22
        self.place.max_guest = 44
        self.place.price_by_night = 1000
        self.place.latitude = 123.4566
        self.place.longitude = -45.6788
        self.place.amenity_ids = ["amenity1", "amenity2"]

        self.assertEqual(self.place.city_id, "1234")
        self.assertEqual(self.place.user_id, "4567")
        self.assertEqual(self.place.name, "Sample Place")
        self.assertEqual(self.place.description, "This is a sample place")
        self.assertEqual(self.place.number_rooms, 33)
        self.assertEqual(self.place.number_bathrooms, 22)
        self.assertEqual(self.place.max_guest, 44)
        self.assertEqual(self.place.price_by_night, 1000)
        self.assertEqual(self.place.latitude, 123.4566)
        self.assertEqual(self.place.longitude, -45.6788)
        self.assertEqual(self.place.amenity_ids, ["amenity1", "amenity2"])


if __name__ == '__main__':
    unittest.main()
