from flask import Flask, request
from datetime import datetime

amazon_killer = Flask(__name__)

USERS_DATABASE = {}
user_counter = 1
CART_DATABASE = {}
cart_counter = 1


class NoSuchUser(Exception):
    def __init__(self, user_id):
        self.user_id = user_id


class NoSuchCart(Exception):
    def __init__(self, cart_id):
        self.cart_id = cart_id


@amazon_killer.route('/users', methods=["POST"])
def create_user():
    global user_counter
    user = request.json
    user['user_id'] = user_counter
    response = {
        "registration_timestamp": datetime.now().isoformat(),
        "user_id": user_counter
    }
    user["registration_timestamp"] = response['registration_timestamp']
    USERS_DATABASE[user_counter] = user

    user_counter += 1

    return response, 201


@amazon_killer.errorhandler(NoSuchUser)
def no_such_user_handler(e):
    return {"error": "no such user with id 1"}, 404


@amazon_killer.route('/users/<int:user_id>')
def get_user(user_id):
    try:
        user = USERS_DATABASE[user_id]
    except KeyError:
        raise NoSuchUser(user_id)
    else:
        return user


@amazon_killer.route('/users/<int:user_id>', methods=["PUT"])
def update_user(user_id):
    user_update = request.json
    try:
        USERS_DATABASE[user_id]['name'] = user_update['name']
        USERS_DATABASE[user_id]['email'] = user_update['email']
    except KeyError:
        raise NoSuchUser
    else:
        return {"status": "success"}, 200


@amazon_killer.route('/users/<int:user_id>', methods=["DELETE"])
def delete_user(user_id):
    try:
        del USERS_DATABASE[user_id]
    except KeyError:
        raise NoSuchUser
    else:
        return {"status": "success"}, 200


@amazon_killer.route('/carts', methods=["POST"])
def create_cart():
    global cart_counter
    cart = request.json
    response = {
        "registration_timestamp": datetime.now().isoformat(),
        "cart_id": cart_counter
    }
    cart["cart_id"] = cart_counter
    cart["registration_timestamp"] = response['registration_timestamp']
    CART_DATABASE[cart_counter] = cart

    cart_counter += 1

    return response, 201


@amazon_killer.route('/carts/<int:cart_id>')
def get_cart(cart_id):
    try:
        cart = CART_DATABASE[cart_id]
    except KeyError:
        raise NoSuchCart(cart_id)
    else:
        return cart


@amazon_killer.errorhandler(NoSuchCart)
def no_such_user_handler(e):
    return {"error": f"no such cart with id {e.cart_id}"}, 404


@amazon_killer.route('/carts/<int:cart_id>', methods=["PUT"])
def update_cart(cart_id):
    cart_update = request.json
    try:
        CART_DATABASE[cart_id]["products"] = cart_update["products"]
    except KeyError:
        raise NoSuchCart
    else:
        return {"status": "success"}, 200


@amazon_killer.route('/carts/<int:cart_id>', methods=["DELETE"])
def delete_cart(cart_id):
    try:
        del CART_DATABASE[cart_id]
    except KeyError:
        raise NoSuchUser
    else:
        return {"status": "success"}, 200


if __name__ == '__main__':
    amazon_killer.run(debug=True)
