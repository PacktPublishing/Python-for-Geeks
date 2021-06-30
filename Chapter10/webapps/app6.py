#app6.py: error and exception handling
import json
from flask import Flask, render_template, abort
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

@app.get('/')
def hello():
    return 'Hello World!'

@app.route('/greeting')
def greeting():
    x = 10/0
    return 'Greetings from Flask web app!'

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('error500.html'), 500

@app.errorhandler(HTTPException)
def generic_handler(error):

    error_detail = json.dumps({
        "code": error.code,
        "name": error.name,
        "description": error.description,
    })
    return render_template('error.html', err_msg=error_detail), error.code

if __name__ == '__main__':
    app.run()
