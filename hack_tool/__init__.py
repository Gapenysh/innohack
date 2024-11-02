__all__ = ("innohack_blueprint",)

from flask import Blueprint

from .client import client_blueprint
from .hr import hr_blueprint

innohack_blueprint = Blueprint("innohack", __name__)
innohack_blueprint.register_blueprint(hr_blueprint)
innohack_blueprint.register_blueprint(client_blueprint)

