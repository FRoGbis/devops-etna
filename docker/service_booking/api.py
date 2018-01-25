import sys
from flask import Flask, request, jsonify
from flasgger import Swagger, swag_from

if len(sys.argv) < 2:
    "print not enough argument"
    exit(1)

PORT = int(sys.argv[1])

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/book', endpoint='book', methods=['GET', 'POST'])
@swag_from('routes/book_avlb.yml', endpoint='book', methods=['GET'])
@swag_from('routes/book_room.yml', endpoint='book', methods=['POST'])
def book():
    return "OK", 200


    
app.run(host='0.0.0.0', port=PORT)
