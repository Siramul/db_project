from flask import jsonify
from app.dao.message import MessageDAO


class MessageHandler:

    def map_to_dict(self, row):
        result = {}
        result['mid'] = row[0]
        result['cid'] = row[1]
        result['sender'] = row[2]
        result['timestamp'] = row[3]
        result['like_dislike_counter'] = row[4]
        result['reply_id'] = row[5]
        result['content'] = row[6]
        result['uri'] = row[7]
        return result

    def get_all_messages(self):
        dao = MessageDAO()
        result = dao.get_all_messages()
        mapped_result = []
        for r in result:
            mapped_result.append(self.map_to_dict(r))
        return jsonify(Message=mapped_result)

    def get_message_by_id(self, message_id):
        dao = MessageDAO()
        result = dao.get_messages_by_id(message_id)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = self.map_to_dict(result)
            return jsonify(Message=mapped)

    def get_message_by_chat_id(self, chat_id):
        dao = MessageDAO()
        result = dao.get_messages_by_chat_id(chat_id)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = self.map_to_dict(result)
            return jsonify(Message=mapped)

    def get_message_by_sender(self, sender):
        dao = MessageDAO()
        result = dao.get_messages_by_sender(sender)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = self.map_to_dict(result)
            return jsonify(Message=mapped)

    def get_message_by_timestamp(self, timestamp):
        dao = MessageDAO()
        result = dao.get_messages_by_timestamp(timestamp)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = self.map_to_dict(result)
            return jsonify(Message=mapped)

    def get_message_by_like_dislike_counter(self, counter):
        dao = MessageDAO()
        result = dao.get_messages_by_likes_dislikes(counter)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = self.map_to_dict(result)
            return jsonify(Message=mapped)

    def get_message_by_like_reply_id(self, counter):
        dao = MessageDAO()
        result = dao.get_messages_by_likes_dislikes(counter)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = self.map_to_dict(result)
            return jsonify(Message=mapped)

    def get_message_by_content(self, text):
        dao = MessageDAO()
        result = dao.get_messages_by_content(text)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = self.map_to_dict(result)
            return jsonify(Message=mapped)

    def get_message_by_media_uri(self, uri):
        dao = MessageDAO()
        result = dao.get_messages_by_media_uri(uri)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = self.map_to_dict(result)
            return jsonify(Message=mapped)