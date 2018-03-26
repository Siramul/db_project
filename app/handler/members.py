from flask import jsonify
from app.dao.contact import ContactDAO
from app.dao.member import MemberDAO

class MemberHandler:

  def getAllMembers(self):
        dao = MemberDAO()
        result = dao.get_all_members()
        mapped_result = []
        for r in result:
            mapped_result.append(self.map_to_dict(r))
        return jsonify(Part=mapped_result)


  def map_to_dict(self, row):
      result = {}
      result['u_id'] = row[0]
      result['chat_id'] = row[1]
      result['primary_key'] = row[2]

      return result