#app4.py: extracting parameters from different requests
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/hello')
@app.route('/hello/<fname> <lname>')
def hello_user(fname=None, lname=None):
    return render_template('app4.html', name=f"{fname} {lname}")

@app.get('/submit')
def process_get_request_data():
    fname = request.args['fname']
    lname = request.args.get('lname', '')
    return render_template('app4.html', name=f"{fname} {lname}")

@app.post('/submit')
def process_post_request_data():
    fname = request.form['fname']
    lname = request.form.get('lname','')
    #lname = request.form['lname']
    return render_template('app4.html', name=f"{fname} {lname}")

if __name__ == '__main__':
    app.run()
