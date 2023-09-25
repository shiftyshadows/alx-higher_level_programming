#!/usr/bin/python3
"""This module defines the City class."""
import sys
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from relationship_state import Base, State


class City(Base):
    """
    Represents a city in a database.

    This class maps to the 'cities' table in the database.

    Attributes:
        id (int): An auto-generated unique identifier for the city.
        name (str): The name of the city (up to 128 characters).
        state_id (int): An integer representing the state to which
        the city belongs, linked to states.id.

    """
    __tablename__ = 'cities'  # Links to the MySQL table named 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
