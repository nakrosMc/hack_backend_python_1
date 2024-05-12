from flask import Flask, jsonify, request, abort
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route("/users", methods=['GET'])
def get_users():
    return jsonify({
        'payload':'success'
    })

@app.route("/user", methods=['POST'])
def post_users():
    return jsonify({
        'payload':'success'
    })

@app.route("/user", methods=['DELETE'])
def delete_users():
    return jsonify({
        'payload':'success'
    })


@app.route("/user", methods=['PUT'])
def put_users():
    return jsonify({
        'payload':'success', 'error': False
    })



@app.route("/api/v1/users", methods=['GET'])
def get_v1_users():
    return jsonify({
        'payload': []
    })


@app.route("/api/v1/user", methods=['POST'])
def post_v1_user():
    if request.method == 'POST':
        # Obtener los parámetros de consulta email y name
        email = request.args.get('email')
        name = request.args.get('name')
        
        # Verificar si se proporcionaron email y name
        if email is None or name is None:
            return jsonify({'error': 'email and name parameters are required'}), 400
        
        # Crear el objeto de respuesta JSON
        response_data = {
            'payload': {
                'email': email,
                'name': name
            }
        }
        
        # Devolver la respuesta JSON
        return jsonify(response_data)

if __name__ == "__main__":
    app.run(debug=True)