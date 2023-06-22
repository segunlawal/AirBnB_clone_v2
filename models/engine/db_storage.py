#!/usr/bin/python3
"""This module contains the DBStorage class"""


from sqlalchemy import create_engine
from os import getenv
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User


class DBStorage:
    """Database engine class"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialization"""
        user = getenv('HBNB_MYSQL_USER')
        passwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        theDB = "mysql+mysqldb://{}:{}@{}/{}".format(user, passwd, host, db)
        self.__engine = create_engine(theDB, pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        classes = [User, State, City, Amenity, Place, Review]
        objects = {}
        if cls is None:
            for cls_name in classes:
                objs = self.__session.query(cls_name)

                for obj in objs:
                    name = obj.__class__.__name__
                    key = "{}.{}".format(name, obj.id)
                    objects.update({key: obj})
        else:
            objs = self.__session.query(cls)
            for obj in objs:
                name = obj.__class__.__name__
                key = "{}.{}".format(name, obj.id)
                objects.update({key: obj})
        return objects

