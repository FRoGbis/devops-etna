from flask import Flask, request, jsonify
from flasgger import Swagger, swag_from
from Database import Database
import requests

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
    
@app.route('/room/<roomId>', methods=['GET'])
@swag_from('routes/room.yml')
def getRoomDetails(roomId):
    rooms = db.getRoom(roomId)
    if rooms == None:
        return "Error while fetching room", 400
    for room, hostel, category in rooms:
        resp = {'room': room.roomId, 'hostel': hostel.name, 'category': category.fullName, 'address': hostel.adress,
                'phone': hostel.tel, 'parking spaces': hostel.parking_space, 'cribs': hostel.crib}
    return jsonify(resp), 200
    
@app.route('/book', methods=['POST'])
@swag_from('routes/book_room.yml')
def bookRoom():
    r = requests.post('http://auth:3000/is_logged', json={'token': request.json['token']})
    if r.status_code == 200:
        return "OK", 200
    else:
        return r.text, 400

app.run(host='0.0.0.0', port=4000, debug=True)
