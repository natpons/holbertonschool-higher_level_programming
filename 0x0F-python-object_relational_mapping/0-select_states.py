#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys


"""stuff only to run when not called via 'import' here"""
if __name__ == '__main__':
    """constructor for creating a connection to the db"""
    connectiondb = MySQLdb.connect(
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3],
        host='localhost',
        port=3306)

    """creates an object that is used for SQL queries and getting the result"""
    cursor = connectiondb.cursor()

    """executes a database query"""
    cursor.execute("SELECT id, name FROM states ORDER BY id ASC")

    """returns the sequence of all records
    remaining in the resulting dataset"""
    query_rows = cursor.fetchall()

    for row in query_rows:
        print(row)
    cursor.close()
    connectiondb.close()
