import flask

app = flask.Flask(__name__)

# https://web.itu.edu.tr/uyar/fad/index.html

@app.route('/hello')
def hello_world():
    return "Hello World!!"

@app.route('/')
def hello():
    return f'<a href="{flask.url_for("hello_world")}">Say hello</a>'

@app.route('/greet_get', methods=['GET'])
def greet_get():
    name = flask.request.args['name']
    surname = flask.request.args['surname']
    return f'<h1>Hello {name} {surname}!!!!</h1>'


@app.route('/greet_post', methods=['POST'])
def greet_post():
    name = flask.request.form['name']
    surname = flask.request.form['surname']
    return flask.render_template("greet.html", name=name, surname=surname)


@app.route('/greet')
def greet():
    return flask.render_template("form.html")


app.run()