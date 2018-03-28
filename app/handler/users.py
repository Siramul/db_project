from flask import jsonify
from app.dao.user import UserDAO


class UserHandler:


    def searchParts(self, args):
        color = args.get('color')
        dao = UserDAO()
        result = dao.searchByColor(color)
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(Part=mapped_result)

    def get_all_users(self):
        P1 = {}
        P1['user_id'] = 1
        P1['first_name'] = 'Joe'
        P1['last_name'] = 'Martin'
        P1['phone_number'] = '7879388245'
        P1['e_mail'] = 'joe.martin@upr.edu'
        P1['user_name'] = 'joe_martin'


        P2 = {}
        P2['pid'] = 456
        P2['price'] = 1.50
        P2['name'] = 'tuerca'

        parts = []
        parts.append(P1)
        parts.append(P2)
        return jsonify(Parts=parts)

    def get_user_by_id(self, id):
        dao = UserDAO()
        result = dao.get_user_by_id(id)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else :
            mapped = self.map_to_dict(result)
            return jsonify(Part=mapped)

    def map_to_dict(self, row):
        result = {}
        result['u_id'] = row[0]
        result['u_fname'] = row[1]
        result['u_lname'] = row[2]
        result['u_phone'] = row[3]
        result['u_email'] = row[4]
        result['username'] = row[5]
        result['u_password'] = row[6]
        return result

    def mapToSupDict(self, row):
        result = {}
        result['sid'] = row[0]
        result['sname'] = row[1]
        return result

    def getAllUsers(self):
        dao = UserDAO()
        result = dao.get_all_users()
        mapped_result = []
        for r in result:
            mapped_result.append(self.map_to_dict(r))
        return jsonify(Part=mapped_result)

    def get_user_by_fname(self, user_fname):
        dao = UserDAO()
        result = dao.get_user_by_fname(user_fname)

        return jsonify(Part=result)


    def get_user_by_lname(self, user_lname):
        dao = UserDAO()
        result = dao.get_user_by_lname(user_lname)

        return jsonify(Part=result)


    def get_user_by_phone(self, user_phone):
        dao = UserDAO()
        result = dao.get_user_by_phone(user_phone)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = self.map_to_dict(result)
            return jsonify(Part=mapped)

    def get_user_by_email(self, uemail):
        dao = UserDAO()
        result = dao.get_user_by_email(uemail)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = self.map_to_dict(result)
            return jsonify(Part=mapped)

    def get_user_by_username(self, username):
        dao = UserDAO()
        result = dao.get_user_by_username(username)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = self.map_to_dict(result)
            return jsonify(Part=mapped)

    def get_user_by_password(self, password):
        dao = UserDAO()
        result = dao.get_user_by_password(password)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = self.map_to_dict(result)
            return jsonify(Part=mapped)