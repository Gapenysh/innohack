__all__ = ("chat_blueprint",)

from flask import Blueprint

from .chat_routes import chat_route

chat_blueprint = Blueprint("chat_main", __name__)
chat_blueprint.register_blueprint(chat_route)