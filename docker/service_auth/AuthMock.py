class AuthMock:
    def registerUser(self, req):
        if 'email' not in req or 'password' not in req or 'firstname' not in req or 'lastname' not in req or 'admin' not in req:
            return False
        if req['email'] == 'string' and req['password'] == 'string':
            return True
        else:
            return False
    
    def loginUser(self, req):
        if 'email' not in req or 'password' not in req:
            return None
        if req['email'] != 'string' or req['password'] != 'string':
            return None
        else:
            rep = {}
            rep['token'] = "0123456789"
            return rep
