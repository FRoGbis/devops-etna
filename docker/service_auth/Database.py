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
            
        
