from app.config.dbconfig import pg_config
import psycopg2


class UsersDao2:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    #List of users in the contact list of some user X
    def getUserConstacts(self, user_id):
        cursor = self.conn.cursor()
        query = """SELECT users.first_name, users.last_name, users.e_mail, users.phone, users.user_name FROM users, contact WHERE contact.user_id = %s AND contact.contact_id = users.user_id"""
        cursor.execute(query, (user_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # List of users in the system
    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = """SELECT first_name, last_name, e_mail, phone, user_name From users"""
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Information on a given user by id
    def getUserInfo(self, user_id):
        cursor = self.conn.cursor()
        query = """SELECT first_name, last_name, e_mail, phone, user_name From users WHERE user_id = %s"""
        cursor.execute(query, (user_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    #Information on a given user by username
    def getUserInfoByUserName(self, user_name):
        cursor = self.conn.cursor()
        query = """SELECT first_name, last_name, e_mail, phone, user_name From users WHERE user_name = %s"""
        cursor.execute(query, (user_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result
