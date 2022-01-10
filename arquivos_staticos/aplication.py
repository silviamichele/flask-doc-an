from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '<p>hello</p>'

@app.route('/my')
@app.route('/my/<nome>')
def function_hi(nome=None):
    return render_template('index.html', name=nome)

if __name__ == '__main__':
    app.run(debug=True)
