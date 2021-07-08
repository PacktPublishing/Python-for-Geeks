#webapp.py: interacting with business latyer via REST API
# for create, delete and list objects
from flask import Flask, render_template, redirect, request
import requests, json

app = Flask(__name__)

#STUDENTS_MS = "http://localhost:8080/students"
STUDENTS_MS = "https://students2-wwzgfqvyaa-de.a.run.app/students"

GRADES_MS = "http://localhost:8000/grades"

@app.get('/')
def list():
    student_svc_resp = requests.get(STUDENTS_MS)
    students = json.loads(student_svc_resp.text)

    grades_svc_resp = requests.get(GRADES_MS)
    grades_list = json.loads(grades_svc_resp.text)

    grades_dict = {grade_item['grade_id']:
                        grade_item for grade_item in grades_list}
    for student in students:
        student['building'] = grades_dict[student['grade']]['building']
        student['teacher'] = grades_dict[student['grade']]['teacher']

    return render_template('main.html', students=students)

@app.post('/')
def add():
    fname = request.form['fname']
    lname = request.form['lname']
    grade = request.form['grade']
    payload = {'name': f"{fname} {lname}", 'grade': grade}
    respone = requests.post(STUDENTS_MS, data=payload)
    return redirect("/")

@app.get('/delete/<int:id>')
def delete(id):
    response = requests.delete(STUDENTS_MS+'/'+str(id))
    return redirect("/")

@app.post('/update/<int:id>')
def update(id):
    fname = request.form['fname']
    lname = request.form['lname']
    grade = request.form['grade']
    payload = {'name' : f"{fname} {lname}", 'grade':grade}
    respone = requests.put(STUDENTS_MS+'/' + str(id), data = payload)
    return redirect("/")

@app.get('/update/<int:id>')
def load_student_for_update(id):
    response = requests.get(STUDENTS_MS+'/'+str(id))
    student = json.loads(response.text)
    fname = student['name'].split()[0]
    lname = student['name'].split()[1]
    return render_template('update.html', fname=fname, lname=lname, student= student)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
