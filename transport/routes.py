from flask import Blueprint
from transport.user_http_adapter import user_adapter, get_user_id

user_bp = Blueprint("user_bp", __name__, url_prefix="/user")

user_bp.add_url_rule("/", view_func=user_adapter, methods=["GET", "POST"])
user_bp.add_url_rule("/<user_id:str>", view_func=get_user_id)
