import unittest
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, ForeignKeyConstraint, Integer, String, Float, Boolean, event, Date

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
    roomId = Column(Integer, primary_key=True, autoincrement=True)
    hostelId = Column(String(50), ForeignKey(Hostel.name))
    categoryId = Column(String(2), ForeignKey(Category.name))
    
class Booking(Base):
    __tablename__ = 'Booking'
    bookingId = Column(Integer, primary_key=True, autoincrement=True)
    roomId = Column(Integer, ForeignKey(Room.roomId))
    userId = Column(String(50), ForeignKey(User.email))
    startDate = Column(Date)
    duration = Column(Integer)
    hasParkingSplace = Column(Boolean)
    hasCrib = Column(Boolean)
    hasRomancePack = Column(Boolean)
    hasBreakfast = Column(Boolean)

class DayCoeff(Base):
    __tablename__ = 'DayCoeff'
    day = Column(String(20), primary_key=True)
    major = Column(Boolean)
    coeff = Column(Float)

@event.listens_for(DayCoeff.__table__, 'after_create')
def dayCoeffInit(target, connection, **kw):
    connection.execute('INSERT INTO DayCoeff(day, major, coeff) VALUES("lundi", 0, 0.0)')
    connection.execute('INSERT INTO DayCoeff(day, major, coeff) VALUES("mardi", 0, 0.0)')
    connection.execute('INSERT INTO DayCoeff(day, major, coeff) VALUES("mercredi", 0, 0.10)')
    connection.execute('INSERT INTO DayCoeff(day, major, coeff) VALUES("jeudi", 0, 0.10)')
    connection.execute('INSERT INTO DayCoeff(day, major, coeff) VALUES("vendredi", 1, 0.15)')
    connection.execute('INSERT INTO DayCoeff(day, major, coeff) VALUES("samedi", 1, 0.15)')
    connection.execute('INSERT INTO DayCoeff(day, major, coeff) VALUES("dimanche", 0, 0.0)')
    
@event.listens_for(Category.__table__, 'after_create')
def createCategories(target, connection, **kw):
    connection.execute('INSERT INTO Category(name, price) VALUES("SR", 1000)')
    connection.execute('INSERT INTO Category(name, price) VALUES("S", 720)')
    connection.execute('INSERT INTO Category(name, price) VALUES("JS", 500)')
    connection.execute('INSERT INTO Category(name, price) VALUES("CD", 300)')
    connection.execute('INSERT INTO Category(name, price) VALUES("CS", 150)')
    
@event.listens_for(Hostel.__table__, 'after_create')
def createHostels(target, connection, **kw):
    connection.execute('INSERT INTO Hostel(name, adress, tel, parking_space, crib) VALUES("Hotel 1", "1 rue aurice", "0322784512", 3, 2)')
    connection.execute('INSERT INTO Hostel(name, adress, tel, parking_space, crib) VALUES("Hotel 2", "12 rue aurice", "0322784513", 2, 2)')
    
@event.listens_for(Room.__table__, 'after_create')
def createRooms(target, connection, **kw):
    connection.execute('INSERT INTO Room(hostelId, categoryId) VALUES("Hotel 1", "S")')
    connection.execute('INSERT INTO Room(hostelId, categoryId) VALUES("Hotel 1", "JS")')
    connection.execute('INSERT INTO Room(hostelId, categoryId) VALUES("Hotel 1", "S")')
    connection.execute('INSERT INTO Room(hostelId, categoryId) VALUES("Hotel 1", "CD")')
    connection.execute('INSERT INTO Room(hostelId, categoryId) VALUES("Hotel 1", "CS")')
    connection.execute('INSERT INTO Room(hostelId, categoryId) VALUES("Hotel 1", "CS")')
    connection.execute('INSERT INTO Room(hostelId, categoryId) VALUES("Hotel 2", "SR")')
    connection.execute('INSERT INTO Room(hostelId, categoryId) VALUES("Hotel 2", "SR")')

class Database:
    def __init__(self, user, password, host):
        self.engine = create_engine('mysql+mysqlconnector://' + user + ':' + password + '@' + host + '/DEVOPS', echo=False)
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
        
    def loginUser(self, user):
        if len(self.session.query(User).filter(User.email == user['email']).filter(User.password == user['password']).all()) == 1:
            return True
        return False
        
    def deleteUser(self, user):
        if len(self.session.query(User).filter(User.email == user['email']).filter(User.password == user['password']).all()) == 1:
            self.session.query(User).filter(User.email == user['email']).filter(User.password == user['password']).delete(synchronize_session=False)
            self.session.commit()
            return True
        return False
        
class DatabaseTest(unittest.TestCase):
        @classmethod
        def setUp(self):
            self.db = Database('devops', 'devops', '127.0.0.1' if 'MYSQL_HOST' not in os.environ else os.environ['MYSQL_HOST'])
            self.u = {}
            self.u['admin'] = True
            self.u['email'] = 'string'
            self.u['password'] = 'string'
            self.u['firstname'] = 'string'
            self.u['lastname'] = 'string'
            
        def test_removeUser(self):
            resp = self.db.deleteUser(self.u)
            self.assertEqual(resp, True)
            
        def test_registerUser(self):
            self.db.deleteUser(self.u)
            resp = self.db.registerUser(self.u)
            self.assertEqual(resp, True)

        def test_loginUser(self):
            self.db.deleteUser(self.u)
            self.db.registerUser(self.u)
            resp = self.db.loginUser(self.u)
            self.assertEqual(resp, True)

if __name__ == '__main__':
    unittest.main()
            
        
