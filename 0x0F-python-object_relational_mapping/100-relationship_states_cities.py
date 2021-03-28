#!/usr/bin/python3
"""Creates the State California with the City San Francisco
from the db hbtn_0e_100_usa"""

import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City


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

    """using the cities = relationship("City", backref="state", ...)
       for the new State obj"""
    new_state = City(name='San Francisco', state=State(name='California'))
    session.add(new_state)

    session.commit()
    session.close()
