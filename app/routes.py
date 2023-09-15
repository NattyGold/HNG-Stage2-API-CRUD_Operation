import os
from  app import create_app, db
from .models import Person
from flask import jsonify, request,abort

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
app.app_context().push()
db.create_all()

# CREATE 
@app.route('/api/person', methods=['POST'])
def create_person():
    if not request.json:
        abort(400)
    person = Person(
        first_name = request.json.get('first_name'),
        last_name = request.json.get('last_name'),
        age = request.json.get('age')
    )
    db.session.add(person)
    db.session.commit()
    return jsonify(person.to_json(), {"message": "created successfully"}), 201

# READ
@app.route("/api/person/<int:id>", methods=["GET"])
def get_personByID(id):
    person = Person.query.get(id)
    if person is None:
        abort(404)
    return jsonify(person.to_json())

#  UPDATE
@app.route('/api/person/update/<int:id>', methods=['PUT'])
def update_person(id):
    if not request.json:
        abort(400)
    person = Person.query.get(id)
    if person is None:
        abort(404)
    person.first_name = request.json.get('first_name', person.first_name)
    person.author = request.json.get('last_name', person.last_name)
    person.price = request.json.get('age', person.age)
    db.session.commit()
    return jsonify(person.to_json(), {"message": "updated successfully"})

#   READ
@app.route("/api/person/<int:id>", methods=["DELETE"])
def delete_person(id):
    person = Person.query.get(id)
    if person is None:
        abort(404)
    db.session.delete(person)
    db.session.commit()
    return jsonify({'message': 'deleted successfully'})