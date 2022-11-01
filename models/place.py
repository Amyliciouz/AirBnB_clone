#!/usr/bin/python3
"""This module contains Place class
that inherits from BaseModel"""
from models.base_model import BaseModel


class Place(BaseModel):
    """ Place class definition
    Attributes:
        city_id (str): The UUID of the city
        user_id (str): The UUID of the user
        name (str): The name of house
        description (str): The description of the house
        number_rooms (int): The number of rooms
        number_bathrooms (int): The number of bathrooms
        max_guest (int): The max_number of guest
        price_by_night (int): The price per night
        latitude (float): The latitude of the place
        longitude (float): The longitude of the place
        amenity_ids: A list of all available amenities
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_id = []
