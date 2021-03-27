#!/usr/bin/python3
"""The script that takes in the name of a state as an argument and lists all
   cities of that state, using the database hbtn_0e_4_usa"""

import MySQLdb
import sys


if __name__ == '__main__':
    connectiondb = MySQLdb.connect(
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3],
        host='localhost',
        port=3306)

    cursor = connectiondb.cursor()

    cursor.execute("SELECT cities.name FROM cities JOIN states "
                   "ON cities.state_id = states.id WHERE states.name=%s"
                   "ORDER BY cities.id ASC", (sys.argv[4],))

    cities_rows = cursor.fetchall()
    """join all tuple items into a string, using a , char as separator"""
    print(", ".join([city[0] for city in cities_rows]))

    cursor.close()
    connectiondb.close()
