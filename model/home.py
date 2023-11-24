"""
This script contains the definition of the Home model
"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Home(Base):
    """
    Class definition of the Home model
    """
    __tablename__ = 'home'

    # Define the columns and their types
    id = Column(Integer, primary_key=True)
    use_kw = Column(Float)
    gen_kw = Column(Float)
    temperature = Column(Float)
    humidity = Column(Float)

    def to_dict(self):
        """ dictionary representation of the Home model """
        new_dict = self.__dict__.copy()
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        return new_dict
