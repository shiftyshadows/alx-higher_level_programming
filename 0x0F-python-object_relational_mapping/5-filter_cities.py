#!/usr/bin/python3
"""
   This module defines a function that takes in the name of a state
   as an argument and lists all cities of that state, using the
   database hbtn_0e_4_usa.
"""
import MySQLdb
import sys


def list_cities_by_state(username, password, database_name, state_name):
    """
    Lists all cities of the specified state from the MySQL database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database_name (str): Name of the MySQL database.
        state_name (str): Name of the state to search for.

    Returns:
        None: This function prints the list of cities to the console.
    """
    try:
        # Connect to MySQL server
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database_name
        )
        # Create a cursor object to interact with the database
        cursor = db.cursor()
        # Execute the query with a parameterized query to prevent SQL injection
        query = """SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s ORDER BY cities.id ASC"""
        cursor.execute(query, (state_name,))
        rows = cursor.fetchall()
        tmp = set(row[0] for row in rows)
        print(*tmp, sep=", ")
        # Close the cursor and database connection
        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py \
            <username> <password> <database_name> <state_name>")
        sys.exit(1)
    username, password, database_name, state_name = sys.argv[1], \
        sys.argv[2], sys.argv[3], sys.argv[4]
    list_cities_by_state(username, password, database_name, state_name)
