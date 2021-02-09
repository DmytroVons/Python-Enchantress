from flask import Flask, request, jsonify
from datetime import datetime


amazon_killer = Flask(__name__)

USERS_DATABASE = {}
user_counter = 1


@amazon_killer.route('/users', methods=["POST"])
def create_user():
    global user_counter
    user = request.json
    response = {
        "registration_timestamp": datetime.now().isoformat(),
        "user_id": user_counter
    }
    user["registration_timestamp"] = response['registration_timestamp']
    USERS_DATABASE[user_counter] = user

    user_counter += 1

    return response, 201


if __name__ == '__main__':
    amazon_killer.run(debug=True)
