#!/usr/bin/python3
"""
   This module defines a function that prints the State
   object with the name passed as argument from the
   database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def find_state_by_name(
      username, password, database_name, state_name_to_search):
    """
    Find and print the State object with the given name from the
    specified database.

    Args:
        username (str): MySQL username for database connection.
        password (str): MySQL password for database connection.
        database_name (str): Name of the MySQL database to connect to.
        state_name_to_search (str): Name of the state to search for.

    Returns:
        None

    """
    # Create a SQLAlchemy engine to connect to the database
    engine = create_engine(
        f"mysql://{username}:{password}@localhost:3306/{database_name}")
    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()
    # Query the database for the State object with the provided name
    state = session.query(State).filter(
        State.name == state_name_to_search).first()
    # Display the State object's id or print "Not found"
    if state:
        print(state.id)
    else:
        print("Not found")


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python find_state.py \
            <username> <password> <database_name> <state_name_to_search>")
        sys.exit(1)
    username, password, database_name, state_name_to_search = sys.argv[1], \
        sys.argv[2], sys.argv[3], sys.argv[4]
    find_state_by_name(username, password, database_name, state_name_to_search)
