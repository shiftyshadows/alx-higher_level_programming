#!/usr/bin/python3
"""
   This module defines a function that prints all City
   objects from the database hbtn_0e_14_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def fetch_cities_by_state(username, password, database_name):
    """
    Fetch and print all City objects from the specified database.

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
    # Query and list all City objects, sorted by id
    s_states = session.query(State).order_by(State.id).all()
    p_cities = session.query(City).order_by(City.id).all()
    # Display the results in the specified format
    for citi in p_cities:
        for state in s_states:
            if state.id == citi.state_id:
                print("{}: ({}) {}".format(state.name, citi.id, citi.name))


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python 14-model_city_fetch_by_state.py \
            <username> <password> <database_name>")
        sys.exit(1)
    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
    fetch_cities_by_state(username, password, database_name)
