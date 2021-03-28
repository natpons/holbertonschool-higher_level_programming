#!/usr/bin/python3
"""Lists all State objects, and corresponding City objects, contained
   in the db hbtn_0e_100_usa"""

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

    states_objs = session.query(State).all()
    for state in states_objs:
        print("{}: {}".format(state.id, state.name))

        """Using the cities = relationship(...) for all State objs"""
        for city in state.cities:
            print("\t" + "{}: {}".format(city.id, city.name))

    session.close()
