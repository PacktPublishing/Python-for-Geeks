# api_app: REST API for student resource
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_restful import Resource, Api, reqparse
import os

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///student.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

parser = reqparse.RequestParser()
parser.add_argument('name', type=str)
parser.add_argument('grade', type=str)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    grade = db.Column(db.String(20), nullable=True)

    def __repr__(self):
        return f"{'id':{self.id}, 'name':{self.name},'grade':{self.grade}}"

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'grade': self.grade
        }


class StudentDao(Resource):
    def get(self, student_id):
        student = Student.query.filter_by(id=student_id).\
            first_or_404(
                description='Record with id={} is not available'.format(student_id))
        return student.serialize()

    def delete(self, student_id):
        student = Student.query.filter_by(id=student_id).\
            first_or_404(
                description='Record with id={} is not available'.format(student_id))
        db.session.delete(student)
        db.session.commit()
        return '', 204

    def put(self, student_id):
        student = Student.query.filter_by(id=student_id).first_or_404(
            description='Record with id={} is not available'.format(student_id))
        args = parser.parse_args()
        name = args['name']
        grade = args['grade']
        if (name):
            student.name = name
        if (grade):
            student.grade = grade
        db.session.commit()
        return student.serialize(), 200


class StudentListDao(Resource):
    def get(self):
        students = Student.query.all()
        return [Student.serialize(student) for student in students]

    def post(self):
        args = parser.parse_args()
        name = args['name']
        grade = args['grade']
        student = Student(name=name, grade=grade)
        db.session.add(student)
        db.session.commit()
        return student.serialize(), 200


api.add_resource(StudentDao, '/students/<student_id>')
api.add_resource(StudentListDao, '/students')


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
