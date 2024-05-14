from flask import Flask, jsonify, request
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
        email = request.args.get('email')
        name = request.args.get('name')
        
        response_data = {
            'payload': {
                'email': email,
                'name': name
            }
        }

        return jsonify(response_data)


@app.route('/api/v1/user/add', methods=['POST'])
def add_user():
    email = request.form.get('email')
    name = request.form.get('name')
    id = request.form.get('id')
    
    return jsonify({
         'payload': {
              'email': email,
              'name': name,
              'id': id
         } 
    })

@app.route('/api/v1/user/create', methods=['POST'])
def create_user():
    # Obtener los datos JSON de la solicitud
    json_data = request.get_json()

    # Obtener los valores de 'email', 'name' e 'id' del diccionario JSON
    email = json_data.get('email')
    name = json_data.get('name')
    user_id = json_data.get('id')
    
    # Devolver una respuesta en formato JSON con los mismos datos recibidos
    return jsonify({
        'payload': {
            'email': email,
            'name': name,
            'id': user_id
        }
    })
        
if __name__ == "__main__":
    app.run(debug=True)