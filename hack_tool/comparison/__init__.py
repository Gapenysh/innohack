__all__ = ("comparison_blueprint",)

from flask import Blueprint

from .comparison_routes import comparison_route

comparison_blueprint = Blueprint("client_main", __name__)
comparison_blueprint.register_blueprint(comparison_route)