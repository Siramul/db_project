from flask import Flask
from app.handler.users import UserHandler
from app.handler.messages import MessageHandler
from app.handler.contacts import ContactHandler
from app.handler.likes import LikeHandler

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello World"


# TODO
@app.route('/login')
def login():
    return "No Login  for you!!!"


@app.route('/UserApp/users')
def users():
        handler = UserHandler()
        return handler.getAllUsers()


# TODO
@app.route('/UserApp/users/id/<int:uid>')
def get_users_by_user_id(uid):
    return UserHandler().get_user_by_id(uid)


# TODO
@app.route('/UserApp/users/fname/<string:ufname>')
def getUsersByFirstName(ufname):
    return UserHandler().get_user_by_fname(ufname)


# TODO
@app.route('/UserApp/users/lname/<string:ulname>')
def getUsersByLastName(ulname):
    return UserHandler().get_user_by_lname(ulname)


# TODO
@app.route('/UserApp/users/phone/<int:uphone>')
def getUsersByPhone(uphone):
    return UserHandler().get_user_by_phone(uphone)


# TODO
@app.route('/UserApp/users/email/<string:uemail>')
def getUsersByEmail(uemail):
    return UserHandler().get_user_by_email(uemail)


# TODO
@app.route('/UserApp/users/username/<string:username>')
def get_users_by_username(username):
    return UserHandler().get_user_by_username(username)


# TODO
@app.route('/UserApp/users/password/<string:password>')
def get_users_by_password(password):
    return UserHandler().get_user_by_password(password)


# TODO
@app.route('/UserApp/contacts')
def get_contacts():
    return ContactHandler().getAllContacts()


# TODO
@app.route('/UserApp/contacts/<int:uid>')
def get_contacts_by_id():
    return ContactHandler().get_contact_by_id()


# TODO
@app.route('/UserApp/users/likes')
def get_likes():
    return LikeHandler().getAllLikes()


# TODO
@app.route('/MessageApp/messages')
def messages():
    return MessageHandler().get_all_messages()


# TODO
@app.route('/MessageApp/messages/mid/<int:mid>')
def get_messages_by_message_id(mid):
    return MessageHandler().get_message_by_id(mid)


# TODO
@app.route('/MessageApp/messages/sender/<int:msender>')
def get_messages_by_sender(msender):
    return MessageHandler().get_message_by_sender(msender)


# TODO
@app.route('/MessageApp/messages/replyid/<int:replyid>')
def get_messages_by_reply_id(replyid):
    return MessageHandler().get_message_by_like_reply_id(replyid)


# TODO
@app.route('/MessageApp/messages/timestamp/<string:timestamp>')
def get_messages_by_timestamp(timestamp):
    return MessageHandler().get_message_by_timestamp(timestamp)


# TODO
@app.route('/MessageApp/messages/content/<string:content>')
def get_messages_by_content(content):
    return MessageHandler().get_message_by_content(content)


# TODO
@app.route('/MessageApp/messages/media/<string:media>')
def get_messages_by_media(media):
    return MessageHandler().get_message_by_media_uri(media)


# TODO
@app.route('/MessageApp/messages/cid/<int:cid>')
def get_messages_by_chat_id(cid):
    return MessageHandler().get_message_by_chat_id(cid)


# TODO
@app.route('/ChatGroupApp/chatGroup')
def chatGroup():
    return "Under construction"


# TODO
@app.route('/ChatGroupApp/chatGroup/<int:cid>')
def getChatGroupByChatID():
    return "Under construction"


# TODO
@app.route('/ChatGroupApp/shatGroup/<string:cname>')
def getChatByChatName():
    return "Under construction"


if __name__ == '__main__':
    app.run()
