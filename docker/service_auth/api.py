import uuid
from flask import Flask, request, session, jsonify
from flasgger import Swagger, swag_from
from Database import Database

app = Flask(__name__)
app.config['SECRET_KEY'] = str(uuid.uuid1())
swagger = Swagger(app)
db = Database("devops", "devops", "mysql")
fake_sess = {}

@app.route('/register_user', methods=['POST'])
@swag_from('routes/register_user.yml')
def registerUser():
    db.registerUser(request.json)
    return "OK", 200
    
@app.route('/login_user', methods=['POST'])
@swag_from('routes/login_user.yml')
def loginUser():
    user = db.loginUser(request.json)
    if user != None:
        token = str(uuid.uuid1())
        session[token] = { 'email': user.email, 'admin': user.admin }
        fake_sess[token] = { 'email': user.email, 'admin': user.admin }
        return jsonify({'token': token}), 200
    else:
        return "Invalid username / password", 400
        
@app.route('/logout', methods=['POST'])
@swag_from('routes/logout.yml')
def logout():
    if request.json['token'] in fake_sess:
        fake_sess.pop(request.json['token'])
        return "Logged out", 200
    else:
        return "Invalid token", 400

@app.route('/is_logged', methods=['POST'])
@swag_from('routes/is_logged.yml')
def isLogged():
    if request.json['token'] in fake_sess:
        return "OK", 200
    else:
        return "Invalid token", 400

app.run(host='0.0.0.0', port=3000, debug=True)
