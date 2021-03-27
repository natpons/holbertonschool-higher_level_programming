#!/usr/bin/python3
"""The script that takes in arguments and displays all values in the states
   table of hbtn_0e_0_usa where name matches the argument
   SAFE from MySQL injections"""

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

    """%s replaced with the value from the tuple,
    automatically escaping the special symbols"""
    cursor.execute("SELECT id, name FROM states "
                   "WHERE name=%s ORDER BY id ASC", (sys.argv[4],))

    query_rows = cursor.fetchall()

    for row in query_rows:
        print(row)
    cursor.close()
    connectiondb.close()
