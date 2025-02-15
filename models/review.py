#!/usr/bin/python3
""" Review module for the HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
import models

if getenv("HBNB_TYPE_STORAGE") == "db":
    class Review(BaseModel, Base):
        """ Review classto store review information """
        __tablename__ = "reviews"
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=True)
else:
    class Review(BaseModel):
        place_id = ""
        user_id = ""
        text = ""