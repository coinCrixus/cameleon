from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    name = Column(String)
    seq = Column(Integer, primary_key=True)

    def __init__(self, name):
        self.name = name
