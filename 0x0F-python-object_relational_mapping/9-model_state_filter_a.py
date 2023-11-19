#!/usr/bin/python3
"""
   This module defines a function that lists all State
   objects that contain the letter a from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def list_states_with_a(username, password, database_name):
    """
    List all State objects containing the letter 'a' from
    the specified database.

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
    # Query and list State objects containing the letter 'a', sorted by id
    states_with_a = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id).all()
    # Display the results
    for state in states_with_a:
        print(f"{state.id}: {state.name}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python list_states_with_a.py \
            <username> <password> <database_name>")
        sys.exit(1)

    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
    list_states_with_a(username, password, database_name)
