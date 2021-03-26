#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa via SQLAlchemy
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

    result = session.query(State).order_by(State.id).first()
    if not result:
        print("Nothing")
    else:
        print("{}: {}".format(result.id, result.name))

    session.close()
