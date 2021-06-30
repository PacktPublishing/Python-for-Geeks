#app1.py: routing in a Flask application
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/greeting')
def greeting():
    return 'Greetings from Flask web app!'

@app.route('/hello/<name>')
def hello_user(name):
    return f'Hello {name}!'

if __name__ == '__main__':
    app.run()
