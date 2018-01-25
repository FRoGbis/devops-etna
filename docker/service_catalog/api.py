import sys
from flask import Flask, request, jsonify
from flasgger import Swagger, swag_from

if len(sys.argv) < 2:
    "print not enough argument"
    exit(1)

PORT = int(sys.argv[1])

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/catalog', methods=['GET'])
@swag_from('routes/catalog.yml')
def catalog():
    return "OK", 200
    
@app.route('/catalog/hotel', methods=['POST'])
@swag_from('routes/add_hotel.yml')
def addHotel():
    return "OK", 200
    
@app.route('/catalog/room', methods=['POST'])
@swag_from('routes/add_room.yml')
def addRoom():
    return "OK", 200
    
app.run(host='0.0.0.0', port=PORT)
