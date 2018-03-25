from flask import Flask, request
from app.handler.parts import PartHandler

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
    return PartHandler().get_user_by_id(uid)


# TODO
@app.route('/UserApp/users/<string:ufname>')
def getUsersByFirstName():
    return "Under construction"


# TODO
@app.route('/UserApp/users/<string:ulname>')
def getUsersByLastName():
    return "Under construction"


# TODO
@app.route('/UserApp/users/<int:uphone>')
def getUsersByPhone():
    return "Under construction"


# TODO
@app.route('/UserApp/users/<string:uemail>')
def getUsersByEmail():
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


@app.route('/PartApp/parts')
def parts():
    if request.args:
        return PartHandler().searchParts(request.args)
    else:
        handler = PartHandler()
        return handler.getAllParts()


@app.route('/PartApp/parts/<int:pid>')
def getPartById(pid):
    return PartHandler().getPartById(pid)


@app.route('/PartApp/parts/<int:pid>/suppliers')
def getSuppliersPartById(pid):
    return PartHandler().getSuppliersByPartId(pid)


if __name__ == '__main__':
    app.run()