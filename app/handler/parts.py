from flask import jsonify
from app.dao.part import PartDAO


class PartHandler:


    def getAllParts1(self):
        parts = ["screw", "wire", "planta"]
        result = ""
        for p in parts:
            result = result + " " + p
        return result

    def get_all_parts(self):
        P1 = {}
        P1['pid'] = 123
        P1['price'] = 0.30
        P1['name'] = 'wire'

        P2 = {}
        P2['pid'] = 456
        P2['price'] = 1.50
        P2['name'] = 'tuerca'

        parts = []
        parts.append(P1)
        parts.append(P2)
        return jsonify(Parts=parts)

    def map_to_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['ufname'] = row[1]
        result['ulname'] = row[2]
        result['uphone'] = row[3]
        result['uemail'] = row[4]
        result['username'] = row[5]
        result['upword'] = row[6]
        return result
    def mapToSupDict(self, row):
        result = {}
        result['sid'] = row[0]
        result['sname'] = row[1]
        return result

    def getAllParts(self):
        dao = PartDAO()
        result = dao.getAllParts()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(Part=mapped_result)

    def get_user_by_id(self, user_id):
        dao = PartDAO()
        result = dao.getUserById(user_id)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = self.map_to_dict(result)
            return jsonify(Part=mapped)


    def getSuppliersByPartId(self, id):
        dao = PartDAO()
        result = dao.getSuppliersByPartId(id)
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToSupDict(r))
        return jsonify(Suppliers=mapped_result)

    def searchParts(self, args):
        color = args.get('color')
        dao = PartDAO()
        result = dao.searchByColor(color)
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(Part=mapped_result)


