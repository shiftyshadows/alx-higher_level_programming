#!/usr/bin/python3
"""
   This module defines a function that lists all cities from the
   database hbtn_0e_4_usa
"""
import MySQLdb
import sys


def list_cities(username, password, database_name):
    """
    Lists all cities from the specified MySQL database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database_name (str): Name of the MySQL database.

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
        # Execute the SQL query to fetch all cities and sort them by cities.id
        cursor.execute("SELECT * FROM cities ORDER BY id ASC")
        # Fetch all rows from the result
        cities = cursor.fetchall()
        # Print the results in the desired format
        for city in cities:
            print(city)
        # Close the cursor and database connection
        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database_name>")
        sys.exit(1)
    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
    list_cities(username, password, database_name)
