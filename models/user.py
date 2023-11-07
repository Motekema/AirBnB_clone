#!/usr/bin/python3
"""Implements the user's models"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Inherits from the BaseModel class and add user functionalities
    Args:
        first_name (str): The first name of the user
        last_name (str): The last name of the user
        email (str): The email of the user
        password (str): The password of the user
    """
    first_name = ""
    last_name = ""
    email = ""
    password = ""

