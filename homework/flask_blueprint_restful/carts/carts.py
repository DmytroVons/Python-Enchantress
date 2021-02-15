from flask import Flask, request, Blueprint
from datetime import datetime

CARTS_DATABASE = {}
cart_counter = 1
cart_bp = Blueprint('carts', __name__)


class NoSuchCart(Exception):
    def __init__(self, cart_id):
        self.cart_id = cart_id


@cart_bp.route('/new', methods=["POST"])
def create_cart():
    global cart_counter
    cart = request.json
    response = {
        "registration_timestamp": datetime.now().isoformat(),
        "cart_id": cart_counter
    }
    cart["cart_id"] = cart_counter
    cart["registration_timestamp"] = response['registration_timestamp']
    CARTS_DATABASE[cart_counter] = cart

    cart_counter += 1

    return response, 201


@cart_bp.route('/get/<int:cart_id>')
def get_cart(cart_id):
    try:
        cart = CARTS_DATABASE[cart_id]
    except KeyError:
        raise NoSuchCart(cart_id)
    else:
        return cart


@cart_bp.errorhandler(NoSuchCart)
def no_such_user_handler(e):
    return {"error": f"no such cart with id {e.cart_id}"}, 404


@cart_bp.route('/update/<int:cart_id>', methods=["PUT"])
def update_cart(cart_id):
    cart_update = request.json
    try:
        CARTS_DATABASE[cart_id]["products"] = cart_update["products"]
    except KeyError:
        raise NoSuchCart
    else:
        return {"status": "success"}, 200


@cart_bp.route('/delete/<int:cart_id>', methods=["DELETE"])
def delete_cart(cart_id):
    try:
        del CARTS_DATABASE[cart_id]
    except KeyError:
        raise NoSuchCart
    else:
        return {"status": "success"}, 200
