#!/usr/bin/python3
"""
Constains the class DBStorage
"""

import model
from model.home import Home, Base
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

class DBStorage:
    """ Interacts with the MySQL database """
    __engine = None
    __session = None

    def __init__(self):
        """ Instantiate DBStorage Object """
        USER = getenv('USER')
        PASSWD = getenv('PASSWD')
        HOST = getenv('HOST')
        DB = getenv('DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(USER,
                                             PASSWD,
                                             HOST,
                                             DB))
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def all(self):
        """ Retrieves all data in the database table """
        objs = self.__session.query(Home).all()
        
        return [obj.to_dict() for obj in objs]

    def get(self, id):
        """ retrieves a specific instance """
        obj = self.__session.query(Home).get(id)
        if obj:
            return obj.to_dict()
        else:
            return None

    def close(self):
        """ close the current session """
        self.__session.remove()
