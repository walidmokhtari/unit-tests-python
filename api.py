from flask import Flask, jsonify, request

app = Flask(__name__)
users = [
    {
        'firstName': 'Walid',
        'lastName': 'MOKHTARI',
        'age': 23
    }
]


@app.route('/')
def home():
    return jsonify(users)


@app.route('/register', methods=['POST'])
def create_user():
    request_data = request.get_json()
    new_user = {
        'firstName': request_data['firstName'],
        'lastName': request_data['lastName'],
        'age': request_data['age'],
    }
    users.append(new_user)
    return jsonify(new_user)

@app.route('/update-user/<string:firstName>', methods=['PUT'])
def update_user(firstName):
    request_data = request.get_json()
    for user in users:
        if(user['firstName'] == firstName):
            user['firstName'] = request_data['firstName']
            user['lastName'] = request_data['lastName']
            user['age'] = request_data['age']
            return jsonify({'message': 'succes'})
    return jsonify({'message': 'user not found'})


@app.route('/user/<string:firstName>')
def get_user_firstName(firstName):
    for user in users:
        if(user['firstName'] == firstName):
            return jsonify({'age': user['age']})
    return jsonify({'message': 'user not found'})


@app.route('/users')
def get_all_users_name():
    return jsonify({'users': users})

app.run(port=5000)
