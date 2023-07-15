#!/usr/bin/python3
"""class City that inherits from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """class that defines a city"""
    state_id = ""
    name = ""
