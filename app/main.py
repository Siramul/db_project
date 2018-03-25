from flask import Flask
from app.handler.users import UserHandler
from app.handler.messages import MessageHandler

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
    return "Under construction"


# TODO
@app.route('/UserApp/users/<int:uid>')
def get_users_by_user_id(uid):
    return UserHandler().get_user_by_id(uid)


# TODO
@app.route('/UserApp/users/<string:ufname>')
def getUsersByFirstName(ufname):
    return "Under construction"


# TODO
@app.route('/UserApp/users/<string:ulname>')
def getUsersByLastName(ulname):
    return "Under construction"


# TODO
@app.route('/UserApp/users/<int:uphone>')
def getUsersByPhone(uphone):
    return "Under construction"


# TODO
@app.route('/UserApp/users/<string:uemail>')
def getUsersByEmail(uemail):
    return "Under construction"


# TODO
@app.route('/UserApp/users/<string:username>')
def get_users_by_username(username):
    return "Under construction"


# TODO
@app.route('/MessageApp/messages')
def messages():
    return MessageHandler().get_all_messages()


# TODO
@app.route('/MessageApp/messages/<int:mid>')
def get_messages_by_message_id(mid):
    return MessageHandler().get_message_by_id(mid)


# TODO
@app.route('/MessageApp/messages/<int:msender>')
def get_messages_by_sender(msender):
    return MessageHandler().get_message_by_sender(msender)


# TODO
@app.route('/MessageApp/messages/<int:replyid>')
def get_messages_by_reply_id(replyid):
    return MessageHandler().get_message_by_like_reply_id(replyid)


# TODO
@app.route('/MessageApp/messages/<string:timestamp>')
def get_messages_by_timestamp(timestamp):
    return MessageHandler().get_message_by_timestamp(timestamp)


# TODO
@app.route('/MessageApp/messages/<string:content>')
def get_messages_by_content(content):
    return MessageHandler().get_message_by_content(content)


# TODO
@app.route('/MessageApp/messages/<string:media>')
def get_messages_by_media(media):
    return MessageHandler().get_message_by_media_uri(media)


# TODO
@app.route('/MessageApp/messages/<int:cid>')
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
