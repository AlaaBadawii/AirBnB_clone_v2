#!/usr/bin/python3
""" Amenity Module for HBNB project """
import os
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.place import place_amenity

storage_type = os.getenv("HBNB_TYPE_STORAGE")
BaseClass = Base if storage_type == "db" else object


class Amenity(BaseModel, BaseClass):
    """ Amenity class """
    if storage_type == "db":
        __tablename__ = "amenities"
        __table_args__ = {
            "mysql_charset": "utf8mb4", # Use full Unicode charset to support all characters including emojis
            "mysql_collate": "utf8mb4_unicode_ci", # Case-insensitive Unicode collation for consistent text sorting/comparisons
        }
        name = Column(String(128), nullable=False)
        place_amenities = relationship(
            "Place",
            secondary=place_amenity,
            viewonly=False,
            back_populates="amenities",
        )
    else:
        name = ""
