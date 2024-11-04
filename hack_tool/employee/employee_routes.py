from flask import Blueprint, jsonify, request

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
        "name": employee,
        "rating": average_rating,
        "role": role,
        "competencies": user_competencies,
        "strong_side": user_strong_side,
        "weak_side": user_weak_side,
        "recommendations": user_recommendations,
        "summary": user_summary
    })


@employee_route.route("/add_review", methods=["POST"])
def create_review():
    user_id = request.json.get("user_id", None)
    review = request.json.get("review", None)

    success = EmployeeBL.create_review(user_id, review)
    if not success:
        return jsonify({"Error": "review wasnt created"})
    else:
        return jsonify({"message": "review was created"})

@employee_route.route("/comparison_list", methods=["GET"])
def comparison_users_list():
    users = EmployeeBL.get_list_users()
    return users

