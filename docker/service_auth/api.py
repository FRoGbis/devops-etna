from flask import Flask, request
from flasgger import Swagger, swag_from
from Database import Database

app = Flask(__name__)
swagger = Swagger(app)
db = Database("devops", "devops", "mysql")

@app.route('/register_user', methods=['POST'])
@swag_from('routes/register_user.yml')
def registerUser():
    db.registerUser(request.json)
    return "OK", 200

app.run(host='0.0.0.0', debug=True)
