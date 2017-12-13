from nameko.rpc import rpc

class RegisterUser(object):
	name = "registerUser"
	
	@rpc
	def registerUser(self, user):
		print ("User : " + user)
		return "Test ok"
