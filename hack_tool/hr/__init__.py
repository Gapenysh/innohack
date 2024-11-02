__all__ = ("hr_blueprint",)

from flask import Blueprint

from .hr_routes import hr_route

hr_blueprint = Blueprint("hr_main", __name__)
hr_blueprint.register_blueprint(hr_route)
