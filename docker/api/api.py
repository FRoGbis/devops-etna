from flask import Flask, request
from flasgger import Swagger, swag_from
from nameko.standalone.rpc import ClusterRpcProxy

app = Flask(__name__)
swagger = Swagger(app)

CONFIG = { 'AMQP_URI': 'amqp://guest:guest@rabbitmq'}

@app.route('/register_user', methods=['POST'])
@swag_from('routes/register_user.yaml')
def register_user():
	a = ""
	with ClusterRpcProxy(CONFIG) as rpc:
		a = rpc.registerUserService.addUser(request.json)
	return a, 200
	
app.run(host='0.0.0.0', debug=True)
