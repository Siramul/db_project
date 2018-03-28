from flask import jsonify
from app.dao.contact import ContactDAO


class ContactHandler:

    def get_all_contacts(self):
        dao = ContactDAO()
        result = dao.get_all_contacts()
        mapped_result = []
        for r in result:
            mapped_result.append(self.map_to_dict(r))
            return jsonify(Part=mapped_result)

    def get_contact_by_id(self, id):
        for r in self.data:
            if id == r[0]:
                return r
            return None

    def map_to_dict(self, row):
        result = {}
        result['u_id'] = row[0]
        result['contact'] = row[1]
        result['primary_key'] = row[2]
        return result
