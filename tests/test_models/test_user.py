#!/usr/bin/python3
"""It tests User class in models"""
import unittest

from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """It test cases against User class"""

    def test_attrs_are_class_attrs(self):
        u_s = User()
        # test that is class attribute
        self.assertTrue(hasattr(User, "first_name")
                        and hasattr(User, "last_name"))
        
    def test_user_is_a_subclass_of_basemodel(self):
        u_s = User()
        self.assertTrue(issubclass(type(u_s), BaseModel))

    def test_class_attrs(self):
        u_s = User()
        self.assertIs(type(u_s.first_name), str)
        self.assertIs(type(u_s.last_name), str)
        self.assertTrue(u_s.first_name == "")
        self.assertTrue(u_s.last_name == "")
