#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa.
It takes 3 arguments: mysql username, mysql password, and database name.
"""

import sys
import MySQLdb

def list_states(username, password, dbname):
    """
    Connect to MySQL database and list all states.
    """
    # Connect to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=dbname)
    cursor = db.cursor()

    # Execute the query
    cursor.execute("SELECT id, name FROM states ORDER BY id ASC")

    # Fetch all the rows in a list of lists
    results = cursor.fetchall()

    # Print the results
    for row in results:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) == 4:
        list_states(sys.argv[1], sys.argv[2], sys.argv[3])

