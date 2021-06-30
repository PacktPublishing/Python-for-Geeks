#app5.py: interacting with db for create, delete and list objects
from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///student.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    grade = db.Column(db.String(20), nullable=True)

    def __repr__(self):
        return '<Student %r>' % self.name

@app.get('/list')
def list_students():
    student_list = Student.query.all()
    return render_template('app5.html', students=student_list)


@app.get('/add')
def add_student():
    fname = request.args['fname']
    lname = request.args.get('lname', '')
    grade = request.args.get('grade','')
    student = Student(name=f"{fname} {lname}", grade=grade)
    db.session.add(student)
    db.session.commit()
    return redirect("/list")

@app.get('/delete/<int:id>')
def del_student(id):
    todelete = Student.query.filter_by(id=id).first()
    db.session.delete(todelete)
    db.session.commit()
    return redirect("/list")

@app.errorhandler(HTTPException)
def page_not_found(error):
    print(error)
    response = error.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": error.code,
        "name": error.name,
        "description": error.description,
    })
    return response

if __name__ == '__main__':
    app.run()
