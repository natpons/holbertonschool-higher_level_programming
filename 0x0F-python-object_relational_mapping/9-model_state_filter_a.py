#!/usr/bin/python3
"""
Lists all State objects that contain the letter a from the db hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


"""Creates a new instance that provides a connection to the DB"""
if __name__ == "__main__":
    engine = create_engine(
             'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                sys.argv[1],
                sys.argv[2],
                sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for row in session.query(State).order_by(State.id):
        if 'a' in row.name:
            print("{}: {}".format(row.id, row.name))

    session.close()
