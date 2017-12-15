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
    hostelId = Column(String(50), ForeignKey(Hostel.name), primary_key=True)
    categoryId = Column(String(2), ForeignKey(Category.name), primary_key=True)   
    
class Booking(Base):
    __tablename__ = 'Booking'
    bookingId = Column(Integer, primary_key=True, autoincrement=True)
    hostelId = Column(String(50))
    categoryId = Column(String(2))
    userId = Column(String(50), ForeignKey(User.email))
    startDate = Column(Date)
    duration = Column(Integer)
    hasParkingSplace = Column(Boolean)
    hasCrib = Column(Boolean)
    hasRomancePack = Column(Boolean)
    hasBreakfast = Column(Boolean)
    ForeignKeyConstraint(['hostelId', 'categoryId'], ['Room.hostelId', 'Room.categoryId'])

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
    
def clean(engine):
    DayCoeff.__table__.drop(engine, checkfirst=True)
    Room.__table__.drop(engine, checkfirst=True)
    Category.__table__.drop(engine, checkfirst=True)
    Hostel.__table__.drop(engine, checkfirst=True)

class Database:
    def __init__(self, user, password, host):
        self.engine = create_engine('mysql+mysqlconnector://' + user + ':' + password + '@mysql/DEVOPS', echo=False)
        clean(self.engine)
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
