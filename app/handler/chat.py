from flask import jsonify
from app.dao.chat import Chat

class ChatHandler:
    def getAllChats(u_id):
        user_chat = Chat(u_id)
        return user_chat.get_all_chats()

    def createChat(u_id, name):
        user_chat = Chat(u_id)
        return jsonify(user_chat.create_chat(name))