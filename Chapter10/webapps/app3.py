#app3.py: rendering static and dynamic contents
from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route('/hello')
def hello():
    hello_url = url_for ('static', filename='app3.html')
    return redirect(hello_url)

@app.route('/greeting')
def greeting():
    msg = "Hello from Python"
    return render_template('app3.html', greeting=msg)

if __name__ == '__main__':
    app.run()
