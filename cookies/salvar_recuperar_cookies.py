from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return '<p>welcome</p>'

@app.route('/cookie/get')
def get_info():
    user = request.cookies.get('username')
    return f'your user: {user}'

@app.route('/cookie/set/<username>')
def set_info(username):
    pass

if __name__ == '__main__':
    app.run(debug=True)
