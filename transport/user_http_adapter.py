from flask import request, jsonfiy
from delivery.user_controller import UserController
from transport.request_interface import RequestUser


def user_adapter():
    if request.method == "POST":
        request_data = request.get_json()
        user_data = RequestUser(request_data)
        response_data = UserController().create_user(user_data)

        return jsonfiy(response_data)
    else:
        users = UserController().get_user_all()

        return jsonfiy(users)

def get_user_id(user_id: str):
    user = UserController().get_user_by_id(user_id)
    return jsonfiy(user)
