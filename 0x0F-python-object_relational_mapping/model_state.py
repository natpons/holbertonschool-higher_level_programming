#!/usr/bin/python3
"""File contains the class definition of a State and an instance
   Base = declarative_base()"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


"""Allows us to create classes that include directives to describe
   the actual database table they will be mapped to"""
Base = declarative_base()


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
