#!/usr/bin/python3
"""
   This module defines a function that adds the State
   object “Louisiana” to the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def add_louisiana(username, password, database_name):
    """
    Add the State object "Louisiana" to the specified database.

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
    # Create a new State with the name "Louisiana".
    louisiana = State(name="Louisiana")
    session.add(louisiana)
    session.commit()
    # Print the new State object's id
    print(louisiana.id)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python add_louisiana.py \
            <username> <password> <database_name>")
        sys.exit(1)
    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
    add_louisiana(username, password, database_name)
