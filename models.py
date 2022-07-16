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

class Person(Base): #database vitra ko table ko information leko 
        __tablename__ = 'table_person'
        person_id = Column(Integer,primary_key = True, index = True)
        person_username = Column ('username',NullType)  #note: string name ra table vitra ko headline ko name same huna parxa
        person_password = Column('password',NullType)
        person_email = Column('email',NullType)
        blog_id = Column('blog_id',NullType)



