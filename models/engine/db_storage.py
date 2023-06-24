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
from sqlalchemy.orm import sessionmaker, scoped_session
        
user = getenv('HBNB_MYSQL_USER')
passwd = getenv('HBNB_MYSQL_PWD')
host = getenv('HBNB_MYSQL_HOST')
db = getenv('HBNB_MYSQL_DB')
        
theDB = "mysql+mysqldb://{}:{}@{}/{}".format(user, passwd, host, db)


class DBStorage:
    """Database engine class"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialization"""
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

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database"""
        current_session = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(current_session)
