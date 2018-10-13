from flask import jsonify
from  app.dao.users_p2 import UsersDao2

class UsersHandler2:

    def build_user_attributes(self, row):
        result = {}
        result['user_id'] = row[0]
        result['first_name'] = row[1]
        result['last_name'] = row[2]
        result['e_mail'] = row[3]
        result['phone'] = row[4]
        result['password']= row[5]
        result['user_name'] = row[6]

        return result

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

    #SignUp. Insert new user.
    # def insertNewUser(self, json):
    #     first_name = json['first_name']
    #     last_name = json['last_name']
    #     e_mail = json['e_mail']
    #     phone = json['phone']
    #     password = json['password']
    #     user_name = json['user_name']
    #
    #     if first_name and last_name and e_mail and phone and password and user_name:
    #         dao = UsersDao2()
    #         user_id = dao.insert(first_name, last_name,  e_mail, phone, password, user_name)
    #         result = self.build_user_attributes(user_id, first_name, last_name, e_mail, phone, password, user_name)
    #         return jsonify(User=result)
    #     else:
    #         return jsonify(Error="Signup went wrong!")



    #Login.
    def accessControl(self, user_name, password):
        username = user_name
        password = password

        if username and password:
            dao = UsersDao2()
            authorization = dao.authorize(username, password)
            if authorization:
                result = self.build_user_attributes(authorization)
                return jsonify(User=result)

            else:
                return jsonify(ERROR='Wrong credentials.')
        else:
            return jsonify(ERROR='Malformed request')


