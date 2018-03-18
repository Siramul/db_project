
from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/lumaris')
def index():
    return "Lumaris is here!"