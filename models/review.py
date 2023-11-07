#!/usr/bin/python3
"""Contains the Review of model"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Implements the Review of model"""
    user_id = ""
    place_id = ""
    text = ""
