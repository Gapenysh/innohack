from flask import jsonify

from hack_tool.dal_models.employee_dal import EmployeeDAL


class EmployeeBL(object):
    @staticmethod
    def get_employees():
        data = EmployeeDAL.get_employees()

        return data

    @staticmethod
    def get_employee(user_id):
        data = EmployeeDAL.get_employee(user_id)

        return data