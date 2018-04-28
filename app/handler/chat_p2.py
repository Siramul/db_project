from flask import jsonify
from  app.dao.chat_p2 import ChatDao


class ChatHandler2:

    def build_message_from_chat_dic(self,row):
        result = {}
        result['message_id'] = row[0]
        result['sender'] = row[1]
        result['content'] = row[2]
        result['reply_id'] = row[3]
        result['time_stamp'] = row[4]
        result['chat_id'] = row[5]
        return result

    def build_users_from_chat_dic(self, row):
        result = {}
        result['user_id'] = row[0]
        result['user_name'] = row[1]
        return result

    def build_all_chats_dic(self,row):
        result = {}
        result['chat_id'] = row[0]
        result['chat_name'] = row[1]
        result['manager'] = row[2]
        return result

    def build_chat_manager_dic(self, row):
        result = {}
        result['first_name'] = row[0]
        result['last_name'] = row[1]
        result['e_mail'] = row[2]
        result['phone'] = row[3]
        result['user_name'] = row[4]
        return result

    # List of messages posted to a chat group
    def getMessagesFromChat(self, chat_id):
        dao = ChatDao()
        messages_list = dao.getMessagesFromChat(chat_id)
        result_list = []
        for row in messages_list:
            result = self.build_message_from_chat_dic(row)
            result_list.append(result)
        return jsonify(Messages=result_list)

    # List of users subscribed to a chat group
    def getUsersFromChat(self, chat_id):
        dao = ChatDao()
        messages_list = dao.getUsersFromChat(chat_id)
        result_list = []
        for row in messages_list:
            result = self.build_users_from_chat_dic(row)
            result_list.append(result)
        return jsonify(Users=result_list)

    # List of chats group in the system
    def getAllChats(self):
        dao = ChatDao()
        messages_list = dao.getAllChats()
        result_list = []
        for row in messages_list:
            result = self.build_all_chats_dic(row)
            result_list.append(result)
        return jsonify(Chats=result_list)


    # Owner of a given chat group
    def getChatManager(self, chat_id):
        dao = ChatDao()
        manager = dao.getChatManager(chat_id)
        result_list = []
        for row in manager:
            result = self.build_chat_manager_dic(row)
            result_list.append(result)
        return jsonify(Manager=result_list)



