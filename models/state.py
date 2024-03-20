#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='delete',backref="state")
    
    if getenv("HBNB_TYPE_STORAGE") != 'db':
        @property
        def cities(self):
            """Getter attribute to retrieve associated cities"""
            from models import storage
            from models.city import City

            lst = []
            for city in storage.all(City).values():
                if city.sate_id == self.id:
                    lst.append(city)
            return lst