from flask import Flask
from flask import request

app = Flask(__name__)

def show_data():
    return '<p>em teoria mostrando um formulário</p>'

def save_data():
    #utilizado se em teoria tivessimos informado dados em um form
    pass

@app.route('/')
def index():
    return '<h1>bem-vindo ao meu site<\h1>'

@app.route('/cadastro', methods=['get', 'post'])
def cadastro():
    if request.method == 'POST':
        return save_data()
    else:
        return show_data()

if __name__ == '__main__':
    app.run()
