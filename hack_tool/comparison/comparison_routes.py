from flask import Blueprint, request, jsonify
from hack_tool.bl_models.comparison_bl import ComparisonBL

comparison_route = Blueprint("comparison_routes", __name__)

@comparison_route.route("/test_comparison", methods=["GET"])
def test_get_all_info_user():
    user_id_1 = request.json.get("user_id_1", None)

    result = ComparisonBL.get_info_about_user(user_id_1)

    return result

@comparison_route.route("/comparison", methods=["GET"])
def comparison_two_users_info():
    user_id_1 = request.json.get("user_id_1", None)
    user_id_2 = request.json.get("user_id_2", None)

    result_1 = ComparisonBL.get_info_about_user(user_id_1)
    result_2 = ComparisonBL.get_info_about_user(user_id_2)

    return jsonify({"1 User": result_1,
                   "2 User":  result_2})

@comparison_route.route("/comparison/ai", methods=["GET"])
def comparison_users_ai():
    user_id_1 = request.json.get("user_id_1", None)
    user_id_2 = request.json.get("user_id_2", None)

    result = ComparisonBL.comparison_two_users_ai(user_id_1, user_id_2)

    return result



