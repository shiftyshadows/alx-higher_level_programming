#!/usr/bin/python3
"""
   This module defines a function that prints the first
   State object from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def print_first_state(username, password, database_name):
    """
    Print the first State object from the specified database.

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
    # Query the first State object without fetching all states
    first_state = session.query(State).order_by(State.id).first()
    # Display the result or print "Nothing" if the table is empty
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python print_first_state.py \
            <username> <password> <database_name>")
        sys.exit(1)

    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
    print_first_state(username, password, database_name)
