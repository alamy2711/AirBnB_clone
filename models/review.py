#!/usr/bin/python3
"""Review  Module defines the Review  class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class representing a review."""

    place_id = ""
    user_id = ""
    text = ""
