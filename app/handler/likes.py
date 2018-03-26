from flask import jsonify
from app.dao.like import LikeDAO




class LikeHandler:

  def getAllLikes(self):
        dao = LikeDAO()
        result = dao.get_all_likes()
        mapped_result = []
        for r in result:
            mapped_result.append(self.map_to_dict(r))
        return jsonify(Part=mapped_result)

  def map_to_dict(self, row):
      result = {}
      result['u_id'] = row[0]
      result['message_id'] = row[1]
      result['like'] = row[2]
      result['primary_key']=row[3]

      return result