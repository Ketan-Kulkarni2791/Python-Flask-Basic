from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_restful import Api, Resource, request
from marshmallow import Schema, fields

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
db = SQLAlchemy(app)
migrate = Migrate(app, db)  # Initializing migrate.
manager = Manager(app)
manager.add_command('db', MigrateCommand)
api = Api(app)


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    age = db.Column(db.Integer, unique=False, nullable=True)


class Company(db.Model):
    cid = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String, unique=True, nullable=False)
    clocation = db.Column(db.String, unique=False, nullable=False)


class EmployeeView(Resource):
    def get(self):
        emp = Employee.query.all()
        return EmployeeSchema().dump(emp, many=True), 200

    def post(self):
        data = request.get_json()
        name = data["name"]
        email = data["email"]

        emp = Employee()
        emp.name = name
        emp.email = email

        db.session.add(emp)

        db.session.commit()

        return EmployeeSchema().dump(emp), 201


class EmployeeSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    email = fields.Str()
    age = fields.Int()


api.add_resource(EmployeeView, '/emp')


if __name__ == "__main__":
    manager.run()       # Calling manager.run() prepares your Manager instance to receive input from the command line.
    app.run(port=5000, debug=True)
