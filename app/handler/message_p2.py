from flask import jsonify
from  app.dao.message_p2 import MessageDao


class MessageHandler2:

    def build_message_dict(self, row):
        result = {}
        result['message_id'] = row[0]
        result['user_name'] = row[1]
        result['content'] = row[2]
        result['reply_id'] = row[3]
        result['time_stamp'] = row[4]
        result['likes'] = row[5]
        result['dislikes'] = row[6]
        return result

    def users_like_dislike_message_dict(self,row):
        result = {}
        result['user_id'] = row[0]
        result['user_name'] = row[1]
        return result

    #List of all messages in the system
    def getAllMessages(self):
        dao = MessageDao()
        messages_list = dao.getAllMessages()
        result_list = []
        for row in messages_list:
            result = self.build_message_dict(row)
            result_list.append(result)
        return jsonify(Messages=result_list)

    # Number of likes to a message
    def getNumberOfLikes(self, message_id):
        dao = MessageDao()
        likes = dao.getNumberOfLikes(message_id)
        return jsonify(Likes=likes)

    # List of users who liked a message
    def getUsersThatLikeAMessage(self, message_id):
        dao = MessageDao()
        messages_list = dao.getUsersThatLikeAMessage(message_id)
        result_list = []
        for row in messages_list:
            result = self.users_like_dislike_message_dict(row)
            result_list.append(result)
        return jsonify(LikedBy=result_list)

    # Number of dislikes to a message
    def getNumberOfDislikes(self, message_id):
        dao = MessageDao()
        dislikes = dao.getNumberOfDislikes(message_id)
        return jsonify(Dislikes=dislikes)

    # List of users who dislikes a message
    def getUsersThatDislikeAMessage(self, message_id):
        dao = MessageDao()
        messages_list = dao.getUsersThatDislikeAMessage(message_id)
        result_list = []
        for row in messages_list:
            result = self.users_like_dislike_message_dict(row)
            result_list.append(result)
        return jsonify(DislikedBy=result_list)
