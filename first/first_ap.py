from flask import Flask
from flask import url_for
#tentando entender o escape
from markupsafe import escape
from flask import request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<p>hello worl!!</p>'

@app.route('/url')
def new_url():
    return '<h1>bem vindo ao meu site</h1>'

@app.route('/<name>')
def youNameHello(name):
    return f'<p>hmmm, hello!! {escape(name)}'

@app.route('/requrl')
def request_url():
    user = request.headers.get('User-Agent')
    return f'<i>{user}</i>'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

# with app.test_request_context():
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#    print(url_for('profile', username='John Doe'))


#para que o server seja ativado com python nome_app.py:
#caso não tenha esse trecho: flask run, ativa
if __name__ == '__main__':
    app.run()
