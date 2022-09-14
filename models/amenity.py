#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
import models


if getenv("HBNB_TYPE_STORAGE") == "db":
    class Amenity(BaseModel, Base):
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        # place_amenities = relationship("Place")
else:
    class Amenity(BaseModel):
        '''Create class Amenity'''
        name = ""