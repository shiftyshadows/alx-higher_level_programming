#!/usr/bin/python3
""" This module defines a function that lists all State objects,
    and corresponding City objects, contained in the database
    hbtn_0e_101_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


def list_states_and_cities(username, password, database_name):
    """
    List all State objects and their corresponding City objects
    from the specified database using relationships.

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
    # Query all State objects and their associated City objects with sorting
    states_and_cities = session.query(State).outerjoin(
        City).order_by(State.id, City.id).all()

    # Display the results in the specified format
    for state in states_and_cities:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script_name.py \
            <username> <password> <database_name>")
        sys.exit(1)
    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
    list_states_and_cities(username, password, database_name)
