#!/usr/bin/python3
"""Lists all states with a name starting with N (upper N)
   from the database hbtn_0e_0_usa"""

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
    cursor.execute("SELECT id, name FROM states " +
                   "WHERE name LIKE 'N%' ORDER BY id ASC")
    query_rows = cursor.fetchall()

    for row in query_rows:
        print(row)
    cursor.close()
    connectiondb.close()
