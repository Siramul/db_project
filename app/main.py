from flask import Flask
from app.handler.users import UserHandler
from app.handler.messages import MessageHandler
from app.handler.contacts import ContactHandler
from app.handler.likes import LikeHandler
from app.handler.replies_to_users import ReplyHandler
from app.handler.chats import ChatHandler
from app.handler.members import MemberHandler
from app.handler.contains import ContainsHandler

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello World"


@app.route('/login')
def login():
    return "No Login  for you!!!"


@app.route('/register/<string:u_name>')
def register(u_name):
    return "User " + u_name + " has been registered"


@app.route('/addContact/<string:contact_name>')
def register_contact(contact_name):
    return "A new Contact" + contact_name + "has been registered"


@app.route('/addContactToChat/<string:contact_name>')
def add_contact_to_chat(contact_name):
    return "User " + contact_name + "has been added to a chat"


@app.route('/removeUserFromChat/<string:u_name>')
def remove_user_from_chat(u_name):
    return "User " + u_name + " has been removed from a chat"


@app.route('/removeUserFromContacts/<string:u_name>')
def remove_user_from_contacts(u_name):
    return "User " + u_name + " has been removed from a contacts list"


# TODO
@app.route('/UserApp/members')
def get_members():
    return MemberHandler().get_all_members()


@app.route('/UserApp/users')
def get_all_users():
    return UserHandler().get_all_users()


@app.route('/UserApp/users/id/<int:uid>')
def get_users_by_user_id(uid):
    return UserHandler().get_user_by_id(uid)


@app.route('/UserApp/users/fname/<string:ufname>')
def get_users_by_first_name(ufname):
    return UserHandler().get_user_by_fname(ufname)


@app.route('/UserApp/users/lname/<string:ulname>')
def get_users_by_last_name(ulname):
    return UserHandler().get_user_by_lname(ulname)


@app.route('/UserApp/users/phone/<int:uphone>')
def get_users_by_phone(uphone):
    return UserHandler().get_user_by_phone(uphone)


@app.route('/UserApp/users/email/<string:uemail>')
def get_users_by_email(uemail):
    return UserHandler().get_user_by_email(uemail)


@app.route('/UserApp/users/username/<string:username>')
def get_users_by_username(username):
    return UserHandler().get_user_by_username(username)


@app.route('/UserApp/users/password/<string:password>')
def get_users_by_password(password):
    return UserHandler().get_user_by_password(password)


@app.route('/UserApp/contacts')
def get_contacts():
    return ContactHandler().get_all_contacts()


@app.route('/UserApp/contacts/<int:uid>')
def get_contacts_by_id():
    return ContactHandler().get_contact_by_id()


@app.route('/UserApp/users/likes')
def get_likes():
    return LikeHandler().get_all_likes()


@app.route('/MessageApp/messages')
def messages():
    return MessageHandler().get_all_messages()


@app.route('/MessageApp/messages/mid/<int:mid>')
def get_messages_by_message_id(mid):
    return MessageHandler().get_message_by_id(mid)


@app.route('/MessageApp/messages/sender/<string:sender>')
def get_messages_by_sender(sender):
    return MessageHandler().get_message_by_sender(sender)


@app.route('/MessageApp/messages/likedislike/<int:counter>')
def get_messages_by_like_dislike(counter):
    return MessageHandler().get_message_by_like_dislike_counter(counter)


@app.route('/MessageApp/messages/replyid/<int:replyid>')
def get_messages_by_reply_id(replyid):
    return MessageHandler().get_message_by_like_reply_id(replyid)


@app.route('/MessageApp/messages/timestamp/<string:timestamp>')
def get_messages_by_timestamp(timestamp):
    return MessageHandler().get_message_by_timestamp(timestamp)


@app.route('/MessageApp/messages/content/<string:content>')
def get_messages_by_content(content):
    return MessageHandler().get_message_by_content(content)


@app.route('/MessageApp/messages/media/<string:media>')
def get_messages_by_media(media):
    return MessageHandler().get_message_by_media_uri(media)


@app.route('/MessageApp/messages/cid/<int:cid>')
def get_messages_by_chat_id(cid):
    return MessageHandler().get_message_by_chat_id(cid)


@app.route('/ReplyToUsersApp/replies')
def get_all_replies():
    return ReplyHandler().get_all_replies()


@app.route('/ReplyToUsersApp/replies/uid/<int:uid>')
def get_replies_by_uid(uid):
    return ReplyHandler().get_replies_by_uid(uid)


@app.route('/ReplyToUsersApp/replies/mid/<int:mid>')
def get_replies_by_mid(mid):
    return ReplyHandler().get_replies_by_mid(mid)


@app.route('/ReplyToUsersApp/replies/uid&mid/<int:uid>/<int:mid>')
def get_replies_by_uid_and_mid(uid,mid):
    return ReplyHandler().get_replies_by_uid_mid(uid, mid)


@app.route('/ChatGroupApp/chats/chatid/<int:cid>')
def get_chat_group_by_chat_id(cid):
    return ChatHandler().get_chats_by_cid(cid)


@app.route('/ChatGroupApp/chats/chatname/<string:cname>')
def get_chat_by_chat_name(cname):
    return ChatHandler().get_chats_by_cname(cname)


@app.route('/ChatGroupApp/chats/chatmanager/<int:cmanager>')
def get_chat_by_chat_manager(cmanager):
    return ChatHandler().get_chats_by_cmanager(cmanager)


# author: Lumaris
# Requirement: Display purposes.
@app.route('/ChatGroupApp/chats')
def get_all_chats():
    return ChatHandler().get_all_chats()


# author: Lumaris
# Requirement: Add a contact to a chat group.
@app.route('/AddUserToChat/<string:user>')
def add_user_to_chat(user):
    return "User " + user + " was added to chat!"


# author:Lumaris
# Requirement: Create a chat group with a given name.
@app.route('/CreateChat/<string:cname>')
def create_chat(cname):
    return "Chat " + cname + " was created!"


# author: Lumaris
# Requirement: Remove a user from a chat group.
@app.route('/RemoveUserFromChat/<string:user>')
def remove_users_from_chat(user):
    return "User " + user + " was removed from chat!"


# author:Lumaris
# Requirement: Remove a chat group.
@app.route('/RemoveChat/<string:cname>')
def remove_chat(cname):
    return "Chat " + cname + " was removed!"


# author:Lumaris
# Requirement: Contains relation display purposes.
@app.route('/ChatMessages')
def display_messages_in_chat():
    return "No messages here!"


@app.route('/ChatApp/<int:uid>/<int:cid>')
def get_chat_by_id(uid, cid):
    return ChatHandler().getChatsById(uid, cid)


@app.route('/LikeMessage')
def like_message():
    return "Message liked!"


@app.route('/DislikeMessage')
def dislike_message():
    return "Message disliked!"


@app.route('/PostMessage/<string:message>')
def post_message(message):
    return "Message " + message + " posted!"


@app.route('/ReplyMessage/<string:reply>')
def post_reply(reply):
    return "Reply " + reply + " posted!"


if __name__ == '__main__':
    app.run(debug=True)
