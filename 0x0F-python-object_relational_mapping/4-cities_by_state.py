#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa"""

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

cursor.execute("SELECT cities.id, cities.name, states.name "
               "FROM cities JOIN states ON cities.state_id = states.id "
               "ORDER BY id ASC")

query_rows = cursor.fetchall()

for row in query_rows:
    print(row)
cursor.close()
connectiondb.close()
