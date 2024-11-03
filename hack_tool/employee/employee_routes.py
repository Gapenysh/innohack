from flask import Blueprint, jsonify

from hack_tool.bl_models.employee_bl import EmployeeBL

employee_route = Blueprint("employee_routes", __name__)


@employee_route.route('/profile/<int:user_id>', methods=['GET'])
def get_employee(user_id):
    employee = EmployeeBL.get_employee(user_id)
    role = EmployeeBL.get_user_role(user_id)
    ratings = EmployeeBL.get_user_rating(user_id)
    average_rating = round(sum(rating[0] for rating in ratings) / len(ratings), 2)
    user_competencies = EmployeeBL.get_user_competencies(user_id)
    user_strong_side = EmployeeBL.get_user_strong_side(user_id)
    user_weak_side = EmployeeBL.get_user_weak_side(user_id)
    user_recommendations = EmployeeBL.get_user_recommendations(user_id)
    user_summary = EmployeeBL.get_user_summary(user_id)


    if employee is None:

        return jsonify({"error": "Employee not found"}), 404

    return jsonify({
        "rating": average_rating,
        "role": role,
        "competencies": user_competencies,
        "strong_side": user_strong_side,
        "weak_side": user_weak_side,
        "recommendations": user_recommendations,
        "summary": user_summary
    })

@employee_route.route("/list_employees", methods=["GET"])
def get_list_employees():
    employees = EmployeeBL.get_list_employees_with_review_count()


    return jsonify(employees)

