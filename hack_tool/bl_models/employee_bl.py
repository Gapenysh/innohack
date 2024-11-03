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
    def add_position_info(user_id, response_json):
        response = json.loads(response_json)
        position = response['role']
        EmployeeDAL.add_position_info(user_id, position)


    @staticmethod
    def add_summary_info(user_id, response_json):
        response = json.loads(response_json)
        content = response['summary']
        EmployeeDAL.add_summary_info(user_id, content)

    @staticmethod
    def add_competencies_info(user_id, response_json):
        response = json.loads(response_json)
        for competency, details in response['parameters'].items():
            rating = details['rating']
            description = details.get('description', None)
            EmployeeDAL.add_competencies_info(user_id, competency, rating, description)

    @staticmethod
    def add_strength_info(user_id, response_json):
        response = json.loads(response_json)
        for strength in response['strengths']:
            EmployeeDAL.add_strength_info(user_id, strength)

    @staticmethod
    def add_weak_info(user_id, response_json):
        response = json.loads(response_json)
        for weakness in response['weaknesses']:
            EmployeeDAL.add_weak_info(user_id, weakness)

    @staticmethod
    def add_recommendation_info(user_id, response_json):
        response = json.loads(response_json)
        for recommendation in response['recommendations']:
            EmployeeDAL.add_recommendation_info(user_id, recommendation)

    @staticmethod
    def get_user_rating(user_id):
        rating = EmployeeDAL.get_user_rating(user_id)

        return rating

    @staticmethod
    def get_user_competencies(user_id):
        user_data = EmployeeDAL.get_user_competencies(user_id)

        return user_data

    @staticmethod
    def get_user_strong_side(user_id):
        user_data = EmployeeDAL.get_user_strong_side(user_id)

        return user_data

    @staticmethod
    def get_user_weak_side(user_id):
        user_data = EmployeeDAL.get_user_weak_side(user_id)

        return user_data

    @staticmethod
    def get_user_recommendations(user_id):
        user_data = EmployeeDAL.get_user_recommendations(user_id)

        return user_data

    @staticmethod
    def get_user_summary(user_id):
        user_data = EmployeeDAL.get_user_recommendations(user_id)

        return user_data

    @staticmethod
    def get_user_role(user_id):
        user_data = EmployeeDAL.get_user_role(user_id)

        return user_data

    @staticmethod
    def get_list_employees_with_review_count():
        data = EmployeeDAL.get_all_employees_with_reviews_count()

        return data
