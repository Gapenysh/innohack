from flask import jsonify, request
from flask import Blueprint

from hack_tool.bl_models.employee_bl import EmployeeBL

hr_route = Blueprint("hr_routes", __name__)


@hr_route.route('/', methods=['GET'])
def get_employees():
    employees = EmployeeBL.get_employees()

    return employees