__all__ = ("innohack_blueprint",)

from flask import Blueprint

from .employee import employee_blueprint
from .hr import hr_blueprint
from .comparison import comparison_blueprint

innohack_blueprint = Blueprint("innohack", __name__)
innohack_blueprint.register_blueprint(hr_blueprint)
innohack_blueprint.register_blueprint(employee_blueprint)
innohack_blueprint.register_blueprint(comparison_blueprint)

