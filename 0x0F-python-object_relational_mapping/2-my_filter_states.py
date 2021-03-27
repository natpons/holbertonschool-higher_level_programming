#!/usr/bin/python3
"""The script that takes in an argument and displays all values in the
   states table of hbtn_0e_0_usa where name matches the argument"""

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
    cursor.execute("SELECT id, name FROM states WHERE "
                   "name='{}' ORDER BY id ASC".format(sys.argv[4]))
    query_rows = cursor.fetchall()

    for row in query_rows:
        print(row)
    cursor.close()
    connectiondb.close()
