from flask import jsonify
from app.dao.contain import Contains


class ContainsHandler:

    def get_all_messages_contained_in_chat(self, c_id):
        user_chat = Contains()
        return jsonify(user_chat.get_all_id_message_contained_in_chat(c_id))
