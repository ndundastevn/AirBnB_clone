#!/usr/bin/python3
"""Unittest model for class User"""

import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test case for User class"""
    def setup(self):
        """sets up the test meethods"""
        self.user = User()

    def test_attributes(self):
        """test if attributes are initialized"""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_attributes_assignment(self):
        """tests if attributes are assigned correctly"""
        user = User()

        user.email = "test@example.com"
        self.assertEqual(user.email, "test@example.com")

        user.password = "password123"
        self.assertEqual(user.password, "password123")

        user.first_name = "John"
        self.assertEqual(user.first_name, "John")

        user.last_name = "Doe"
        self.assertEqual(user.last_name, "Doe")

        if __name__ == '__main__':
            unittest.main()
