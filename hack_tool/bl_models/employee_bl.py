from flask import jsonify
import json

from hack_tool.dal_models.hr_dal import HrDal
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

    @staticmethod
    def add_summary_for_all_users():
        users = EmployeeDAL.get_employees()
        for user_id in users:
            review = HrDal.get_reviews_by_id(user_id)
            """надо доделать"""


    @staticmethod
    def add_summary_info(user_id, response_json):
        response = json.loads(response_json)
        content = response['summary']
        EmployeeDAL.add_summary_info(user_id, content)

    @staticmethod
    def add_competencies_info(user_id, response_json):
        response = json.loads(response_json)
        for competency, rating in response['parameters'].items():
            EmployeeDAL.add_competencies_info(user_id, competency, rating)

    @staticmethod
    def add_strength_info(user_id, response_json):
        response = json.loads(response_json)
        for strength in response['strengths']:
            EmployeeDAL.add_strength_info(user_id, strength)

    @staticmethod
    def add_weak_info(user_id, response_json):
        response = json.loads(response_json)
        for weakness in response['weaknesses']:
            EmployeeDAL.add_strength_info(user_id, weakness)

    @staticmethod
    def add_recommendation_info(user_id, response_json):
        response = json.loads(response_json)
        for recommendation in response['recommendations']:
            EmployeeDAL.add_strength_info(user_id, recommendation)
