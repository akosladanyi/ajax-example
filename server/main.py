from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/', methods=['GET'])
def root():
    return app.send_static_file('index.html')


@app.route('/tooltip/<rectname>', methods=['GET'])
def rect_tooltip(rectname):
    dct = {
        'r1': '<a href="http://hup.hu">alma</a>',
        'r2': '<strong>körte</string>',
        'r3': ('<table class="table-tooltip">'
               '<tr>'
               '<th>First</th>'
               '<th>Second</th>'
               '</tr>'
               '<tr>'
               '<td>szőlő</td>'
               '<td>5</td>'
               '</tr>'
               '</table>')
    }
    try:
        msg = dct[rectname]
    except KeyError:
        msg = ''
    return jsonify(message=msg)
