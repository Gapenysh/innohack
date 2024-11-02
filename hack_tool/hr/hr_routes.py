from flask import jsonify, request
from flask import Blueprint

from hack_tool.bl_models.employee_bl import EmployeeBL

hr_route = Blueprint("hr_routes", __name__)


@hr_route.route('/employees', methods=['GET'])
def get_employees():
    employees = EmployeeBL.get_employees()

    return employees


@hr_route.route('/employees/<int:user_id>', methods=['GET'])
def get_employee(user_id):
    employee = EmployeeBL.get_employee(user_id)

    if employee is None:
        # Возвращаем 404, если сотрудник не найден
        return jsonify({"error": "Employee not found"}), 404

    # Если сотрудник найден, возвращаем его данные
    return jsonify(employee), 200