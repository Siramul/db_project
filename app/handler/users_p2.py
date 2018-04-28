from flask import jsonify
from  app.dao.users_p2 import UsersDao2

class UsersHandler2:

    def build_contacts_dic(self, row):
        result = {}
        result['first_name'] = row[0]
        result['last_name'] = row[1]
        result['e_mail'] = row[2]
        result['phone'] = row[3]
        result['user_name'] = row[4]
        return result

    # List of users in the contact list of some user X
    def getUserContacts(self, user_id):
        dao = UsersDao2()
        contacts_list = dao.getUserConstacts(user_id)
        result_list = []
        for row in contacts_list:
            result = self.build_contacts_dic(row)
            result_list.append(result)
        return jsonify(Contacts=result_list)

    #List of users in the system
    def getAllUsers(self):
        dao = UsersDao2()
        users_list = dao.getAllUsers()
        result_list = []
        for row in users_list:
            result = self.build_contacts_dic(row)
            result_list.append(result)
        return jsonify(Users=result_list)


    # Information on a given user by id
    def getUserInfo(self, user_id):
        dao = UsersDao2()
        users_list = dao.getUserInfo(user_id)
        result_list = []
        for row in users_list:
            result = self.build_contacts_dic(row)
            result_list.append(result)
        return jsonify(UserInfo=result_list)


    def getUserInfoByUserName(self, user_name):
        dao = UsersDao2()
        users_list = dao.getUserInfoByUserName(user_name)
        result_list = []
        for row in users_list:
            result = self.build_contacts_dic(row)
            result_list.append(result)
        return jsonify(UserInfo=result_list)

