#!/usr/bin/python3
"""File contains the class definition of a State and an instance
   Base = declarative_base()"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import Base, City


class State(Base):
    """Class State that inherits from Base"""
    __tablename__ = 'states'
    id = Column(Integer,
                nullable=False,
                primary_key=True,
                autoincrement="auto",
                unique=True)
    name = Column(String(128),
                  nullable=False)

    """- cities: represent a relationship with the class City
       - if the State obj is deleted, all linked City objs must be auto deleted
       - the reference from a City object to his State should be named state"""
    cities = relationship("City", backref="state", cascade="all, delete")
