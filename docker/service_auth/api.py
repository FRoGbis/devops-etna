from flask import Flask, request, jsonify
from flasgger import Swagger, swag_from

from AuthMock import AuthMock
mock = AuthMock()

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/register_user', methods=['POST'])
@swag_from('routes/register_user.yml')
def registerUser():
    if mock.registerUser(request.json):
        return "OK", 200
    else:
        return "Invalid fields", 400
    
@app.route('/login_user', methods=['POST'])
@swag_from('routes/login_user.yml')
def login_user():
    rep = mock.loginUser(request.json)
    if rep == None:
        return "Invalid login", 400
    return jsonify(rep), 200
    
app.run(host='0.0.0.0', port=3000)
