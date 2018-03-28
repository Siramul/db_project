from flask import jsonify
from app.dao.chat import ChatDAO

class ChatHandler:

    def map_to_dict(self, row):
        result = {}
        result['chat_id'] = row[0]
        result['name'] = row[1]
        result['manager'] = row[2]

        return result

    def get_all_chats(self):
        dao = ChatDAO()
        result = dao.get_all_chats()
        mapped_result = []
        for r in result:
            mapped_result.append(self.map_to_dict(r))
        return jsonify(Message=mapped_result)

    def get_chats_by_chat_id(self, c_id):
        dao = ChatDAO()
        result = dao.get_chat_by_cid(c_id)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = self.map_to_dict(result)
            return jsonify(Chat=mapped)

    def get_chats_by_chat_name(self, cname):
        dao = ChatDAO()
        result = dao.get_chat_by_cname(cname)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = self.map_to_dict(result)
            return jsonify(Chat=mapped)

    def get_chats_by_chat_manager(self, cmanager):
        dao = ChatDAO()
        result = dao.get_chat_by_cmanager(cmanager)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = self.map_to_dict(result)
            return jsonify(Chat=mapped)
