from flask import jsonify, request
from flask import Blueprint

from hack_tool.bl_models.employee_bl import EmployeeBL
from hack_tool.bl_models.hr_bl import HrBl

hr_route = Blueprint("hr_routes", __name__)


@hr_route.route('/employees', methods=['GET'])
def get_employees():
    employees = EmployeeBL.get_list_employees_with_review_count()


    return employees


@hr_route.route('/employees/<int:user_id>', methods=['GET'])
def get_employee(user_id):

    employee = EmployeeBL.get_employee(user_id)

    if employee is None:

        return jsonify({"error": "Employee not found"}), 404


    return jsonify(employee), 200

@hr_route.route('/employees/<int:user_id>/summary', methods=['GET'])
def get_employee_summary(user_id):
    summary = HrBl.create_summary(user_id)

    if summary is None:

        return jsonify({"error": "Summary can't creatable"}), 404


    return jsonify(summary), 200