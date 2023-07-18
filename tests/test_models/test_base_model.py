#!/usr/bin/python3
import unittest
from datetime import datetime
from base_model import BaseModel
import os

class TestBaseModel(unittest.TestCase):
    def test_init_with_arguments(self):
        """Test initialization of BaseMode"""
        id_value = "123"
        created_at = datetime.now()
        updated_at = datetime.now()
        kwargs = {
            "id": id_value,
            "created_at": created_at,
            "updated_at": updated_at
        }

        model = BaseModel(**kwargs)

        self.assertEqual(model.id, id_value)
        self.assertEqual(model.created_at, created_at)
        self.assertEqual(model.updated_at, updated_at)

    def test_init_without_arguments(self):
        """Test initialization of BaseModel without any any arguments"""
        model = BaseModel()

        self.assertIsNotNone(model.id)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_str_representation(self):
        """Test string representation of BaseModel object"""
        model = BaseModel()
        expected_str = f"[BaseModel] ({model.id}) {model.__dict__}"
        self.assertEqual(str(model), expected_str)

    def test_save_method(self):
        """Test save method of BaseModel class"""
        model = BaseModel()
        old_updated_at = model.updated_at

        model.save()

        self.assertNotEqual(model.updated_at, old_updated_at)

    def test_to_dict_method(self):
        """Test to_dict method"""
        model = BaseModel()
        obj_dict = model.to_dict()

        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['id'], model.id)
        self.assertEqual(obj_dict['created_at'], model.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], model.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
