from app.config.dbconfig import pg_config
import psycopg2


class ChatDao:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)


    # List of messages posted to a chat group
    def getMessagesFromChat(self, chat_id):
        cursor = self.conn.cursor()
        query = """SELECT * FROM message natural inner join contains WHERE chat_id = %s;"""
        cursor.execute(query, (chat_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # List of users subscribed to a chat group
    def getUsersFromChat(self, chat_id):
        cursor = self.conn.cursor()
        query = """SELECT user_id, user_name FROM users natural inner join member WHERE chat_id = %s;"""
        cursor.execute(query, (chat_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # List of chats group in the system
    def getAllChats(self):
        cursor = self.conn.cursor()
        query = """Select * FROM chat;"""
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


    # Owner of a given chat group
    def getChatManager(self, chat_id):
        cursor = self.conn.cursor()
        query = """Select first_name, last_name, e_mail, phone, user_name FROM chat, users WHERE chat.manager = users.user_id AND chat_id = %s;"""
        cursor.execute(query, (chat_id,))
        result = cursor.fetchall()
        return result
