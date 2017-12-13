from nameko.rpc import rpc

class RegisterUserService(object):
    name = 'registerUserService'
    
    @rpc
    def registerUser(self, user):
        return rpc.databaseService.addUser(user)
