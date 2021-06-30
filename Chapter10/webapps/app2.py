#app2.py: map request with method type
from flask import Flask, request

app = Flask(__name__)

@app.route('/submit', methods=['GET'])
def req_with_get():
    return "Received a get request"

@app.post('/submit')
def req_with_post():
    return "Received a post request"

@app.route('/submit2', methods = ['GET', 'POST'])
def both_get_post():
    if request.method == 'POST':
        return "Received a post request 2"
    else:
        return "Received a get request 2"

if __name__ == '__main__':
    app.run()
