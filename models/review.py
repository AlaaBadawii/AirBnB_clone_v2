#!/usr/bin/python3
""" Review module for the HBNB project """
import os
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel, Base

storage_type = os.getenv("HBNB_TYPE_STORAGE")
BaseClass = Base if storage_type == "db" else object


class Review(BaseModel, BaseClass):
    """ Review classto store review information """
    if storage_type == "db":
        __tablename__ = "reviews"
        __table_args__ = {
            "mysql_charset": "utf8mb4",
            "mysql_collate": "utf8mb4_unicode_ci",
        }
        place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        text = Column(String(1024), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
