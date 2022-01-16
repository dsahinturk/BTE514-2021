import flask

app = flask.Flask(__name__)

books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

@app.route('/')
def hello():
    return 'Welcome to books API!!!'


@app.route('/api/books', methods = ['GET'])
def get_all():
    return flask.jsonify(books)


@app.route('/api/book', methods=['POST'])
def get_by_id():
    id = int(flask.request.form['id'])

    for a_book in books:
        if id == a_book['id']:
            return flask.jsonify(a_book)

    return ""

app.run()