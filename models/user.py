#!/usr/bin/python3
"""User Module defines the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """User class representing user data."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
