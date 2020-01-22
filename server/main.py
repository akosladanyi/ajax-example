from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/', methods=['GET'])
def root():
    return app.send_static_file('index.html')


@app.route('/tooltip/<rectname>', methods=['GET'])
def rect_tooltip(rectname):
    dct = {'r1': 'alma', 'r2': 'körte', 'r3': 'szőlő'}
    try:
        msg = dct[rectname]
    except KeyError:
        msg = ''
    return jsonify(message=msg)
