import sys
from flask import Flask, request, jsonify
from flasgger import Swagger, swag_from

if len(sys.argv) < 2:
    "print not enough argument"
    exit(1)

PORT = int(sys.argv[1])

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/price', methods=['GET'])
@swag_from('routes/price.yml')
def price():
    return "OK", 200
    
@app.route('/price/room', methods=['PATCH'])
@swag_from('routes/price_room.yml')
def priceRoom():
    return "OK", 200
    
@app.route('/price/increase', methods=['PATCH'])
@swag_from('routes/price_increase.yml')
def priceIncrease():
    return "OK", 200

    
app.run(host='0.0.0.0', port=PORT)
