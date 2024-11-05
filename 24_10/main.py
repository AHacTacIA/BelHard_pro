from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

@app.route('/test1/')
def test1():
    return '<h1>Test1</h1>'

app.run()