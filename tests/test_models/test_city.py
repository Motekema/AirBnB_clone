#!/usr/bin/python3
"""It test for city class of models.city."""
import unittest

from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """It test cases for City class"""

    def setUp(self):
        self.city = City()
        self.attr_list = ["state_id", "name"]

    def test_attrs_are_class_attrs(self):
        for attr in self.attr_list:
            self.assertFalse(bool(getattr(self.city, attr)))
            self.assertIs(type(getattr(self.city, attr)), str)
            
    def test_city_is_a_subclass_of_basemodel(self):
        self.assertTrue(issubclass(type(self.city), BaseModel))
