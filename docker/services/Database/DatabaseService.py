from nameko.rpc import rpc
from Database import Database

class DatabaseService(object):
    name = 'databaseService'
    database = Database("devops", "devops", "localhost")
	
    @rpc
    def addUser(self, user):
        return self.database.registerUser(user)
