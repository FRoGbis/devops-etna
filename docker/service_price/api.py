from flask import Flask, request, jsonify
from flasgger import Swagger, swag_from

from PriceMock import PriceMock
mock = PriceMock()

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/price', methods=['POST'])
@swag_from('routes/price.yml')
def price():
    price = mock.price(request.json)
    if price == None:
        return "Invalid request", 400
    return jsonify(price), 200

    
app.run(host='0.0.0.0', port=5000)
