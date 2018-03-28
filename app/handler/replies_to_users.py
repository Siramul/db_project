from flask import jsonify
from app.dao.reply_to_user import ReplyDAO


class ReplyHandler:

    def map_to_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['mid'] = row[1]
        return result

    def get_all_replies(self):
        dao = ReplyDAO()
        result = dao.get_all_replies()
        mapped_result = []
        for r in result:
            mapped_result.append(self.map_to_dict(r))
        return jsonify(Reply=mapped_result)

    def get_replies_by_uid(self, uid):
        dao = ReplyDAO()
        result = dao.get_replies_by_uid(uid)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = self.map_to_dict(result)
            return jsonify(Reply=mapped)

    def get_replies_by_mid(self, mid):
        dao = ReplyDAO()
        result = dao.get_replies_by_mid(mid)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = self.map_to_dict(result)
            return jsonify(Reply=mapped)

    def get_replies_by_uid_mid(self, uid, mid):
        dao = ReplyDAO()
        result = dao.get_replies_by_uid_and_mid(uid, mid)
        if result is None:
            return jsonify(Error="NOT FOUND")
        else:
            mapped = self.map_to_dict(result)
            return jsonify(Reply=mapped)