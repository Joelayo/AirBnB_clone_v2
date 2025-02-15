#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
import models
from models.city import City


if getenv("HBNB_TYPE_STORAGE") == "db":
    class State(BaseModel, Base):
        """ State class """
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship('City')
else:
    class State(BaseModel):
        """ Defined class to work with FileStorage'"""
        name = ''
        cities = models.storage.all(City)