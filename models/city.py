#!/usr/bin/python3
"""City Module defines the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """City class representing a city."""

    state_id = ""
    name = ""
