from flask import Flask, request, jsonify
from flasgger import Swagger, swag_from

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/book', methods=['POST'])
@swag_from('routes/book.yml')
def book():
    return "OK", 200

    
app.run(host='0.0.0.0', port=6000)
