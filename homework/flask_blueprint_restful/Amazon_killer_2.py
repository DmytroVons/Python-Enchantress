from flask import Flask, Blueprint
from flask_restful import Api
from users.users import Users
from carts.carts import cart_bp

amazon_killer = Flask(__name__)
api = Api(amazon_killer)

api.add_resource(Users, '/users', '/users/<int:user_id>')
amazon_killer.register_blueprint(cart_bp, url_prefix="/carts")

if __name__ == '__main__':
    amazon_killer.run(debug=True)
