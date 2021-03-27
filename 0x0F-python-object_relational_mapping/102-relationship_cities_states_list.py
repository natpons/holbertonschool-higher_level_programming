#!/usr/bin/python3
"""Lists all City objects from ANOTHER database hbtn_0e_101_usa"""

import sys
from model_state import Base, State
from model_city import City
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

    for city, state in session.query(City, State).filter(
                                     City.state_id == State.id):
        print("{}: {} -> {}".format(city.id, city.name, state.name))

    session.close()
