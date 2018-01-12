from flask import Flask, request, jsonify
from flasgger import Swagger, swag_from
from Database import Database

app = Flask(__name__)
swagger = Swagger(app)
db = Database("devops", "devops", "mysql")

@app.route('/rooms', methods=['GET'])
@swag_from('routes/rooms.yml')
def getRooms():
    rooms = db.getRooms()
    resp = {}
    resp['rooms'] = []
    for room, hostel, category in rooms:
        resp['rooms'].append({'id': room.roomId, 'hostel': hostel.name, 'category': category.fullName})
    return jsonify(resp), 200

app.run(host='0.0.0.0', port=4000, debug=True)
