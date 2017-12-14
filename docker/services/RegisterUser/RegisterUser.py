from nameko.rpc import rpc, RpcProxy

class RegisterUserService(object):
    name = 'registerUserService'
    dbSrv = RpcProxy('databaseService')
    
    @rpc
    def registerUser(self, user):
        return self.dbSrv.addUser(user)
        return True
