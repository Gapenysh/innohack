__all__ = ("employee_blueprint",)

from flask import Blueprint

from .employee_routes import employee_route

employee_blueprint = Blueprint("employee_main", __name__)
employee_blueprint.register_blueprint(employee_route)
