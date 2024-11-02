__all__ = ("client_blueprint",)

from flask import Blueprint

from .client_routes import client_route

client_blueprint = Blueprint("client_main", __name__)
client_blueprint.register_blueprint(client_route)
