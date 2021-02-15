from flask import Flask, request, Blueprint
from datetime import datetime
from flask_restful import Resource

USERS_DATABASE = {}
user_counter = 1


class NoSuchUser(Exception):
    def __init__(self, user_id):
        self.user_id = user_id


class Users(Resource):
    @staticmethod
    def post():
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

    @staticmethod
    def get(user_id):
        try:
            user = USERS_DATABASE[user_id]
        except KeyError:
            return {"error": "no such user with id 1"}, 404
        else:
            return user

    @staticmethod
    def put(user_id):
        user_update = request.json
        try:
            USERS_DATABASE[user_id]['name'] = user_update['name']
            USERS_DATABASE[user_id]['email'] = user_update['email']
        except KeyError:
            raise NoSuchUser
        else:
            return {"status": "success"}, 200

    @staticmethod
    def delete(user_id):
        try:
            del USERS_DATABASE[user_id]
        except KeyError:
            raise NoSuchUser
        else:
            return {"status": "success"}, 200
