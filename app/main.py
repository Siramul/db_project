from flask import Flask, request, render_template
from app.handler.users import UserHandler
from app.handler.chat import ChatHandler

app = Flask(__name__, template_folder='template')

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
    return "Under construction"


# TODO
@app.route('/MessageApp/messages/<int:mid>')
def getMessagesByMessageID():
    return "Under construction"


# TODO
@app.route('/MessageApp/messages/<int:msender>')
def getMessagesBySender():
    return "Under construction"


# TODO
@app.route('/MessageApp/messages/<int:replyid>')
def getMessagesByReplyID():
    return "Under construction"


# TODO
@app.route('/MessageApp/messages/<string:timestamp>')
def getMessagesByTimestamp():
    return "Under construction"


# TODO
@app.route('/MessageApp/messages/<string:content>')
def getMessagesByContent():
    return "Under construction"


# TODO
@app.route('/MessageApp/messages/<string:media>')
def getMessagesByMedia():
    return "Under construction"


# TODO
@app.route('/MessageApp/messages/<int:cid>')
def getMessagesByChatID():
    return "Under construction"

@app.route('/AllChats/<int:uid>')
def allAllUserChats(uid):
    return render_template('project_webpage.html', chats = ChatHandler.getAllChats(uid))

@app.route('/CreateChat/<int:uid>/<string:cname>')
def createChat(uid, cname):
    return ChatHandler.createChat(uid, cname)

# TODO
@app.route('/ChatGroupApp/chatGroup/<int:cid>')
def getChatGroupByChatID():
    return "Under construction"


# TODO
@app.route('/ChatGroupApp/shatGroup/<string:cname>')
def getChatByChatName():
    return "Under construction"


if __name__ == '__main__':
    app.run(debug = True)