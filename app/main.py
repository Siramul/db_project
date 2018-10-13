from flask import Flask, jsonify, request

from app.handler.message_p2 import MessageHandler2
from app.handler.chat_p2 import ChatHandler2
from app.handler.users_p2 import UsersHandler2
from flask_cors import CORS

app = Flask(__name__)

CORS(app)


@app.route('/')
def home():
    return "Hello World"


# @app.route('/login')
# def login():
#     return "No Login  for you!!!"
#
#
# @app.route('/register/<string:u_name>')
# def register(u_name):
#     return "User " + u_name + " has been registered"
#
#
# @app.route('/addContact/<string:contact_name>')
# def register_contact(contact_name):
#     return "Contact " + contact_name + " has been registered"
#
#
# @app.route('/addContactToChat/<string:contact_name>')
# def add_contact_to_chat(contact_name):
#     return "User " + contact_name + " has been added to a chat"
#
#
# @app.route('/removeUserFromChat/<string:u_name>')
# def remove_user_from_chat(u_name):
#     return "User " + u_name + " has been removed from a chat"
#
#
# @app.route('/removeUserFromContacts/<string:u_name>')
# def remove_user_from_contacts(u_name):
#     return "User " + u_name + " has been removed from contacts list"
#
#
# @app.route('/MemberApp/members')
# def get_members():
#     return MemberHandler().get_all_members()
#
#
# @app.route('/UserApp/users')
# def get_all_users():
#     return UserHandler().get_all_users()
#
#
# @app.route('/UserApp/users/id/<int:uid>')
# def get_users_by_user_id(uid):
#     return UserHandler().get_user_by_id(uid)
#
#
# @app.route('/UserApp/users/fname/<string:ufname>')
# def get_users_by_first_name(ufname):
#     return UserHandler().get_user_by_fname(ufname)
#
#
# @app.route('/UserApp/users/lname/<string:ulname>')
# def get_users_by_last_name(ulname):
#     return UserHandler().get_user_by_lname(ulname)
#
#
# @app.route('/UserApp/users/phone/<string:uphone>')
# def get_users_by_phone(uphone):
#     return UserHandler().get_user_by_phone(uphone)
#
#
# @app.route('/UserApp/users/email/<string:uemail>')
# def get_users_by_email(uemail):
#     return UserHandler().get_user_by_email(uemail)
#
#
# @app.route('/UserApp/users/username/<string:username>')
# def get_users_by_username(username):
#     return UserHandler().get_user_by_username(username)
#
#
# @app.route('/UserApp/users/password/<string:password>')
# def get_users_by_password(password):
#     return UserHandler().get_user_by_password(password)
#
#
# @app.route('/UserApp/contacts')
# def get_contacts():
#     return ContactHandler().get_all_contacts()
#
#
# @app.route('/UserApp/contacts/uid/<int:uid>')
# def get_contacts_by_id(uid):
#     return ContactHandler().get_contact_by_uid(uid)
#
#
# @app.route('/UserApp/users/likes')
# def get_likes():
#     return LikeHandler().get_all_likes_dislikes()
#
#
# @app.route('/MessageApp/messages')
# def messages():
#     return MessageHandler().get_all_messages()
#
#
# @app.route('/MessageApp/messages/mid/<int:mid>')
# def get_messages_by_message_id(mid):
#     return MessageHandler().get_message_by_id(mid)
#
#
# @app.route('/MessageApp/messages/sender/<string:sender>')
# def get_messages_by_sender(sender):
#     return MessageHandler().get_message_by_sender(sender)
#
#
# @app.route('/MessageApp/messages/likedislike/<int:counter>')
# def get_messages_by_like_dislike(counter):
#     return MessageHandler().get_message_by_like_dislike_counter(counter)
#
#
# @app.route('/MessageApp/messages/replyid/<int:replyid>')
# def get_messages_by_reply_id(replyid):
#     return MessageHandler().get_message_by_like_reply_id(replyid)
#
#
# @app.route('/MessageApp/messages/timestamp/<string:timestamp>')
# def get_messages_by_timestamp(timestamp):
#     return MessageHandler().get_message_by_timestamp(timestamp)
#
#
# @app.route('/MessageApp/messages/content/<string:content>')
# def get_messages_by_content(content):
#     return MessageHandler().get_message_by_content(content)
#
#
# @app.route('/MessageApp/messages/media/<int:media>')
# def get_messages_by_media(media):
#     return MessageHandler().get_message_by_media_uri(media)
#
#
# @app.route('/MessageApp/messages/cid/<int:cid>')
# def get_messages_by_chat_id(cid):
#     return MessageHandler().get_message_by_chat_id(cid)
#
#
# @app.route('/ReplyToUsersApp/replies')
# def get_all_replies():
#     return ReplyHandler().get_all_replies()
#
#
# @app.route('/ReplyToUsersApp/replies/uid/<int:uid>')
# def get_replies_by_uid(uid):
#     return ReplyHandler().get_replies_by_uid(uid)
#
#
# @app.route('/ReplyToUsersApp/replies/mid/<int:mid>')
# def get_replies_by_mid(mid):
#     return ReplyHandler().get_replies_by_mid(mid)
#
#
# @app.route('/ReplyToUsersApp/replies/uid&mid/<int:uid>/<int:mid>')
# def get_replies_by_uid_and_mid(uid,mid):
#     return ReplyHandler().get_replies_by_uid_mid(uid, mid)
#
#
# @app.route('/ChatGroupApp/chats/cid/<int:cid>')
# def get_chat_group_by_chat_id(cid):
#     return ChatHandler().get_chats_by_chat_id(cid)
#
#
# @app.route('/ChatGroupApp/chats/cname/<string:cname>')
# def get_chat_by_chat_name(cname):
#     return ChatHandler().get_chats_by_chat_name(cname)
#
#
# @app.route('/ChatGroupApp/chats/cmanager/<int:cmanager>')
# def get_chat_by_chat_manager(cmanager):
#     return ChatHandler().get_chats_by_chat_manager(cmanager)
#
#
# # author: Lumaris
# # Requirement: Display purposes.
# @app.route('/ChatGroupApp/chats')
# def get_all_chats():
#     return ChatHandler().get_all_chats()
#
#
# # author: Lumaris
# # Requirement: Add a contact to a chat group.
# @app.route('/AddUserToChat/<string:user>')
# def add_user_to_chat(user):
#     return "User " + user + " was added to chat!"
#
#
# # author:Lumaris
# # Requirement: Create a chat group with a given name.
# @app.route('/CreateChat/<string:cname>')
# def create_chat(cname):
#     return "Chat " + cname + " was created!"
#
#
# # author: Lumaris
# # Requirement: Remove a user from a chat group.
# @app.route('/RemoveUserFromChat/<string:user>')
# def remove_users_from_chat(user):
#     return "User " + user + " was removed from chat!"
#
#
# # author:Lumaris
# # Requirement: Remove a chat group.
# @app.route('/RemoveChat/<string:cname>')
# def remove_chat(cname):
#     return "Chat " + cname + " was removed!"
#
#
# # author:Lumaris
# # Requirement: Contains relation display purposes.
# @app.route('/ChatMessages')
# def display_messages_in_chat():
#     return "No messages here!"
#
#
# @app.route('/LikeMessage')
# def like_message():
#     return "Message liked!"
#
#
# @app.route('/DislikeMessage')
# def dislike_message():
#     return "Message disliked!"
#
#
# @app.route('/PostMessage/<string:message>')
# def post_message(message):
#     return "Message " + message + " posted!"
#
#
# @app.route('/ReplyMessage/<string:reply>')
# def post_reply(reply):
#     return "Reply " + reply + " posted!"

#################### Phase2###################


#List of all messages in the system
@app.route('/MessagesApp/messages')
def getallparts():
    return MessageHandler2().getAllMessages()


# Number of likes to a message
@app.route('/MessagesApp/likes/<int:message_id>')
def getnumberoflikes(message_id):
    return MessageHandler2().getNumberOfLikes(message_id)


# List of users who liked a message
@app.route('/MessagesApp/likedby/<int:message_id>')
def getusersthatlikeamessage(message_id):
    return MessageHandler2().getUsersThatLikeAMessage(message_id)


# Number of dislikes to a message
@app.route('/MessagesApp/dislikes/<int:message_id>')
def getnumberofdislikes(message_id):
    return MessageHandler2().getNumberOfDislikes(message_id)

# List of users who dislikes a message
@app.route('/MessagesApp/dislikedby/<int:message_id>')
def getusersthatdislikeamessage(message_id):
    return MessageHandler2().getUsersThatDislikeAMessage(message_id)

# List of messages posted to a chat group
@app.route('/ChatApp/messages/<int:chat_id>')
def getmessagesfromchat(chat_id):
    return ChatHandler2().getMessagesFromChat(chat_id)

#List of users subscribed to a chat group
@app.route('/ChatApp/users/<int:chat_id>')
def getusersfromchat(chat_id):
    return ChatHandler2().getUsersFromChat(chat_id)

#List of chats group in the system
@app.route('/ChatApp/chats')
def getallchats():
    return ChatHandler2().getAllChats()

#Owner of a given chat group
@app.route('/ChatApp/manager/<int:chat_id>')
def getchatmanager(chat_id):
    return ChatHandler2().getChatManager(chat_id)

#List of users in the contact list of some user X
@app.route('/UserApp/contacts/<int:user_id>')
def getusercontacts(user_id):
    return UsersHandler2().getUserContacts(user_id)

#List of users in the system
@app.route('/UserApp/users')
def getallusers():
    return UsersHandler2().getAllUsers()

@app.route('/UserApp/<string:user_name>')
def getuserinfobyusername(user_name):
    return UsersHandler2().getUserInfoByUserName(user_name)

# Information on a given user by id
@app.route('/UserApp/<int:user_id>')
def getuserinfo(user_id):
    return UsersHandler2().getUserInfo(user_id)


@app.route('/SignUp', methods=['POST'])
def signUp():
    return UsersHandler2().insertNewUser(request.json)

@app.route('/Login', methods=['POST'])
def login():
    return UsersHandler2().accessControl(request.get_json('data'))





if __name__ == '__main__':
    app.run(debug=True)
