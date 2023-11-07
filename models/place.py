#!/usr/bin/python3
"""Contains the Place of model"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Implements the Place of model
    Args:
        user_id (str): the User id.
        city_id (str): the City id.
        name (str): the name of the place.
        description (str): the description of the place.
        price_by_night (int): the price by night of the place.
        number_rooms (int): the number of rooms of the place.
        number_bathrooms (int): the number of bathrooms of the place.
        max_guest (int): the maximum number of guests of the place.
        latitude (float): the latitude of the place.
        longitude (float): the longitude of the place.
        amenity_ids (list): A list of Amenity ids.
    """
    user_id = ""
    city_id = ""
    name = ""
    description = ""
    price_by_night = 0
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
