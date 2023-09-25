#!/usr/bin/python3
""" This module defines the class State. """
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Create a declarative base
Base = declarative_base()


class State(Base):
    """
    Represents a state in a database.

    This class maps to the 'states' table in the database.

    Attributes:
        id (int): An auto-generated unique identifier for the state.
        name (str): The name of the state (up to 128 characters).

    """
    __tablename__ = 'states'  # Links to the MySQL table named 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City", back_populates="state", cascade="all, delete-orphan")
