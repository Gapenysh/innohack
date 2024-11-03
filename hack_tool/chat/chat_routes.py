from flask import Blueprint, request


chat_route = Blueprint("chat_routes", __name__)


@chat_route.route("/chat", methods=["GET"])
def ask_to_chat():
    query = request.json.get("query", None)

    result = ChatBl.query_to_ask()

    return result
