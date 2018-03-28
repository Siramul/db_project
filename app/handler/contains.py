from flask import jsonify
from app.dao.contains import Contains

class ContainsHandler:
    def getAllIdMessageContainedInChat(self, c_id):
        user_chat = Contains(c_id)
        return jsonify(user_chat.get_all_id_message_contained_in_chat(c_id))
