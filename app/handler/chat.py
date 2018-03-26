from flask import jsonify
from app.dao.chat import Chat

class ChatHandler:
    def getAllChats(u_id):
        user_chat = Chat(u_id)
        return jsonify(user_chat.get_all_chats())

    def createChat(u_id, name):
        user_chat = Chat(u_id)
        return jsonify(user_chat.create_chat(name))

    def addContactToChat(u_id, c_id, u_id_to_add):
        user_chat = Chat(u_id)
        return jsonify(user_chat.add_contact_to_chat(c_id, u_id_to_add))

    def removeUserFromChat(u_id, c_id, u_id_to_remove):
        user_chat = Chat(u_id)
        return jsonify(user_chat.remove_user_from_chat(c_id, u_id_to_remove))

    def removeChat(u_id, c_id):
        user_chat = Chat(u_id)
        return jsonify(user_chat.remove_chat(c_id))