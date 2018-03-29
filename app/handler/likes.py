from flask import jsonify
from app.dao.like import LikeDAO


class LikeHandler:
    def get_all_likes_dislikes(self):
        dao = LikeDAO()
        result = dao.get_all_likes_dislikes()
        mapped_result = []
        for r in result:
            mapped_result.append(self.map_to_dict(r))
        return jsonify(Likes=mapped_result)

    def map_to_dict(self, row):
        result = {}
        result['u_id'] = row[0]
        result['message_id'] = row[1]
        result['like'] = row[2]
        result['primary_key']=row[3]
        return result

    def get_all_likes_dislikes_by_user_id(self, uid):
        dao = LikeDAO()
        result = dao.get_likes_by_user_id(uid)
        if result is None:
            return jsonify(Error='NOT FOUND'), 404
        else:
            mapped = self.map_to_dict(result)
            return jsonify(Likes=mapped)

    def get_all_likes_dislikes_by_message_id(self, mid):
        dao = LikeDAO()
        result = dao.get_likes_by_message_id(mid)
        if result is None:
            return jsonify(Error='NOT FOUND'), 404
        else:
            mapped = self.map_to_dict(result)
            return jsonify(Likes=mapped)

    def get_all_likes(self):
        dao = LikeDAO()
        result = dao.get_all_likes()
        mapped_result = []
        for r in result:
            if r is None:
                return jsonify(Error='NOT FOUND'), 404
            else:
                # mapped_result.append(self.map_to_dict(r))
                return jsonify(Likes=result)

    def get_all_dislikes(self):
        dao = LikeDAO()
        result = dao.get_all_dislikes()
        mapped_result = []
        for r in result:
            mapped_result.append(self.map_to_dict(r))
        return jsonify(Likes=mapped_result)
