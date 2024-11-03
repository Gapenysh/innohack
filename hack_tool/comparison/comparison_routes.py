from flask import Blueprint, request
from hack_tool.bl_models.comparison_bl import ComparisonBL

comparison_route = Blueprint("comparison_routes", __name__)

@comparison_route.route("/comparison", methods=["GET"])
def comparison_users():
    user_id_1 = request.json.get("user_id_1", None)
    user_id_2 = request.json.get("user_id_2", None)

    result = ComparisonBL.get_info_two_users(user_id_1, user_id_2)

    return result
@comparison_route.route("/comparison/ai", methods=["GET"])
def comparison_users():
    user_id_1 = request.json.get("user_id_1", None)
    user_id_2 = request.json.get("user_id_2", None)

    result = ComparisonBL.comparison_users_by_id_ai(user_id_1, user_id_2)

    return result



