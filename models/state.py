#!/usr/bin/python3
""" State Module for HBNB project """
import os
from sqlalchemy import Column, String
from models.city import City

from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship

storage_type = os.getenv("HBNB_TYPE_STORAGE")
BaseClass = Base if storage_type == "db" else object


class State(BaseModel, BaseClass):
    """ State class """
    if storage_type == 'db':
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """ Instantiates a new State """
        super().__init__(*args, **kwargs)

    if storage_type != "db":
        @property
        def cities(self):
            """getter for list of city instances related to the state"""
            from models import storage
            city_list = []
            all_cities = storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
