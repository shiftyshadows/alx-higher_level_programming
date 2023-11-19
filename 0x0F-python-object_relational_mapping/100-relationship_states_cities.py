#!/usr/bin/python3
"""
   This module defines a function that creates the State “California”
   with the City “San Francisco” from the database hbtn_0e_100_usa.
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)


def add_california_with_sf(username, password, database_name):
    """
    Add the State "California" with the City "San Francisco" to the
    specified database using relationships.

    Args:
        username (str): MySQL username for database connection.
        password (str): MySQL password for database connection.
        database_name (str): Name of the MySQL database to connect to.

    Returns:
        None

    """
    # Create a SQLAlchemy engine to connect to the database
    engine = create_engine(
        f"mysql://{username}:{password}@localhost:3306/{database_name}")
    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()
    # Create the state "California"
    california = State(name="California")
    # Create the city "San Francisco" and establish the relationship
    san_francisco = City(name="San Francisco", state=california)
    # Add the new state and city to the session
    session.add(california)
    session.add(san_francisco)
    # Commit the changes to the database
    session.commit()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python 100-relationship_states_cities.py \
            <username> <password> <database_name>")
        sys.exit(1)
    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
    add_california_with_sf(username, password, database_name)
