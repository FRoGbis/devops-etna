from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Boolean

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    email = Column(String(50), primary_key=True)
    firstname = Column(String(255))
    lastname = Column(String(255))
    password = Column(String(255))
    admin = Column(Boolean)

class Category(Base):
    __tablename__ = 'Category'
    name = Column(String(2), primary_key=True)
    price = Column(Float())
    
class Hostel(Base):
    __tablename__ = 'Hostel'
    name = Column(String(50), primary_key=True)
    adress = Column(String(255))
    tel = Column(String(255))
    parking_space = Column(Integer)
    crib = Column(Integer)
    
class Room(Base):
    __tablename__ = 'Room'
    hostelId = Column(String(50), ForeignKey(Hostel.name), primary_key=True)
    categoryId = Column(String(2), ForeignKey(Category.name), primary_key=True)
    

class Database:
    def __init__(self, user, password, host):
        self.engine = create_engine('mysql+mysqlconnector://' + user + ':' + password + '@mysql/DEVOPS', echo=False)
        Base.metadata.create_all(self.engine)
        Base.metadata.bind = self.engine
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def registerUser(self, user):
        user = User(email=user['email'], lastname=user['lastname'], firstname=user['firstname'], password=user['password'], admin=user['admin'])
        try:
            self.session.add(user)
            self.session.commit()
        except:
            self.session.rollback()
            raise
        return True
