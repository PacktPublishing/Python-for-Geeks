#webapp.py: interacting with business latyer via REST API
# for create, delete and list objects
from flask import Flask, render_template, redirect, request
import requests, json

app = Flask(__name__)

@app.get('/')
def list():
    response = requests.get('http://localhost:8080/students')
    data = json.loads(response.text)
    return render_template('main.html', students=data)

@app.post('/')
def add():
    fname = request.form['fname']
    lname = request.form['lname']
    grade = request.form['grade']
    payload = {'name': f"{fname} {lname}", 'grade': grade}
    respone = requests.post('http://localhost:8080/students', data=payload)
    return redirect("/")

@app.get('/delete/<int:id>')
def delete(id):
    response = requests.delete('http://localhost:8080/students/'+str(id))
    return redirect("/")

@app.post('/update/<int:id>')
def update(id):
    fname = request.form['fname']
    lname = request.form['lname']
    grade = request.form['grade']
    payload = {'name' : f"{fname} {lname}", 'grade':grade}
    respone = requests.put('http://localhost:8080/students/' + str(id), data = payload)
    return redirect("/")

@app.get('/update/<int:id>')
def load_student_for_update(id):
    response = requests.get('http://localhost:8080/students/'+str(id))
    student = json.loads(response.text)
    fname = student['name'].split()[0]
    lname = student['name'].split()[1]
    return render_template('update.html', fname=fname, lname=lname, student= student)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
