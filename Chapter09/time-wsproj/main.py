
from flask import Flask
from datetime import date, datetime


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in file `main.py`. This is the case in our yaml file
app = Flask(__name__)


@app.route('/')
def welcome():
    return 'Welcome Python Geek! Use appropriate URI for date and time'


@app.route('/date')
def today():
    today = date.today()
    return "{date:" + today.strftime("%B %d, %Y") + '}'


@app.route('/time')
def time():
    now = datetime.now()
    return "{time:" + now.strftime("%H:%M:%S") + '}'


if __name__ == '__main__':
    # For local testing
    app.run(host='127.0.0.1', port=8080, debug=True)
