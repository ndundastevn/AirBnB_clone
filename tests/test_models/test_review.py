#!/usr/bin/python3
"""Unittest module for the Review Class."""

import unittest
from datetime import datetime
import time
from models.review import Review
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    def setUp(self):
        # Set up an instance of Review clase
        self.review = Review()

    def tearDown(self):
        # Clean up the instance of Review clase 
        del self.review

    def test_attributes_initialization(self):
        # Check if the attributes are initialized correctly
        self.assertEqual(self.review.place_id, "")  # Empty string
        self.assertEqual(self.review.user_id, "")  # Empty string
        self.assertEqual(self.review.text, "")  # Empty string


if __name__ == '__main__':
    unittest.main()
