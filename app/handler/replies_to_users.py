from flask import jsonify
from app.dao.reply_to_user import ReplyDAO

class ReplyHandler:

    def map_to_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['mid'] = row[1]
        return result

    def get_all_replies(self):
        dao = ReplyDAO
        result = dao.get_all_replies()
        mapped_result = []
        for r in result:
            mapped_result.append(self.map_to_dict(r))
        return jsonify(Reply=mapped_result)

    def get_r