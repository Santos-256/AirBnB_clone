#!/usr/bin/python3
"""Defines the City class of the AirBnB platform."""

from models.base_model import BaseModel


class City(BaseModel):
    """Represents the city.

    Attributes:
        state_id (str): The state id.
        name (str): The state name.
    """

    state_id = ""
    name = ""
