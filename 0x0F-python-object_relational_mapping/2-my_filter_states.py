#!/usr/bin/python3
"""This module defines a function that takes in an argument and
displays all values in the states table of hbtn_0e_0_usa where
name matches the argument."""
import MySQLdb
import sys


def search_states_by_name(username, password, database_name, state_name):
    """
    Displays all values in the states table where the
    name matches the provided state name.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database_name (str): Name of the MySQL database.
        state_name (str): State name to search for.

    Returns:
        None: This function prints the list of matching states to the console.
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
        # Execute the query to fetch states matching the provided state name
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        cursor.execute(query, (state_name,))
        # Fetch all rows from the result
        matching_states = cursor.fetchall()
        # Print the results in the desired format
        for state in matching_states:
            print(state)
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
    username, password, database_name, state_name_searched = \
        sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    search_states_by_name(
        username, password, database_name, state_name_searched)
