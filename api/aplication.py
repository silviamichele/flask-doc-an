from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return '<p>welcome</p>'

@app.route('/get_data')
def get_data():
    # return {
    #     'teste': 123,
    #     'interno': 'mjk',
    #     'cod': '12edasSAS'
    # }

    # return json.dumps([{
    #     'teste': 123,
    #     'interno': 'mjk',
    #     'cod': '12edasSAS'
    # }, {
    #     'teste':2312,
    #     'interno':'sipa',
    #     'cod':'dgyeh'}])

    return jsonify([{
        'teste': 123,
        'interno': 'mjk',
        'cod': '12edasSAS'
    }, {
        'teste':2312,
        'interno':'sipa',
        'cod':'dgyeh'}])

if __name__ == '__main__':
    app.run()
