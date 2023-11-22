from flask import Flask, request, jsonfiy
from delivery.user_controller import UserController
from domain.user import User
from dataclasses import dataclass


app = Flask(__name__)

@app.route("/users", method=["POST"])
def create_user():
    request_data = request.get_json()
    user_data = User("", request_data.get("email"), request_data.get("password"), request_data.get("name"), request_data.get("description"))

    response_data = UserController().create_user(user_data)

    return jsonfiy(response_data)



# @dataclass
# class RequestCreateUser