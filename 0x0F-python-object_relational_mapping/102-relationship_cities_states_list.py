#!/usr/bin/python3
"""
   This module defines a function that hat lists all City
   objects from the database hbtn_0e_101_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


def list_cities(username, password, database_name):
    """
    List all City objects from the specified database using relationships.

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
    # Query all City objects & associated State objects
    cities = session.query(City).order_by(City.id).all()
    # Display the results in the specified format
    for city in cities:
        print(f"{city.id}: {city.name} ({city.state.name})")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script_name.py \
            <username> <password> <database_name>")
        sys.exit(1)
    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
    list_cities(username, password, database_name)
