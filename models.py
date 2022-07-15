from sqlalchemy import Column , MetaData ,Integer
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
metadata =  MetaData()

class student(Base):
    __tablename__='student'
    id = Column(Integer,primary_key=True ,index=True)
    first_name=Column('firstname',NullType)
    last_name=Column('lastname',NullType)
    dob=Column('dob' ,NullType)
    #table sanga connect gareko i.e table ko kura lai api sanga link gareko


