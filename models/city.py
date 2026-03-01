#!/usr/bin/python3
""" City Module for HBNB project """
import os

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

storage_type = os.getenv("HBNB_TYPE_STORAGE")
BaseClass = Base if storage_type == "db" else object


class City(BaseModel, BaseClass):
    """ The city class, contains state ID and name """
    if storage_type == 'db':
        __tablename__ = "cities"

        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship("Place", backref="city", cascade="all, delete")
    else:
        name = ""
        state_id = ""

    def __init__(self, *args, **kwargs):
        """ Instantiates a new City """
        super().__init__(*args, **kwargs)
