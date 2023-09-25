#!/usr/bin/python3
"""
   This module defines a function that changes the name of
   a State object from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def change_state_name(username, password, database_name):
    """
    Change the name of a State object in the specified database.

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
    # Query the State object with id = 2
    state_to_update = session.query(State).filter_by(id=2).first()
    # Update the name of the State object to "New Mexico"
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()
    else:
        print("State with id 2 not found")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python change_state_name.py \
            <username> <password> <database_name>")
        sys.exit(1)
    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
    change_state_name(username, password, database_name)
