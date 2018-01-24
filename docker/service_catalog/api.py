from flask import Flask, request, jsonify
from flasgger import Swagger, swag_from

from CatalogMock import CatalogMock
mock = CatalogMock()

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/catalog', methods=['GET'])
@swag_from('routes/catalog.yml')
def catalog():
    return jsonify(mock.catalog()), 200

    
app.run(host='0.0.0.0', port=4000)
