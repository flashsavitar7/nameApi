from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://namesofpips_user:Ii8wUXW1CCnKu4KSkiTr6rm0plkGpcHM@dpg-cjv22795mpss738pq8vg-a.oregon-postgres.render.com/namesofpips'  # Replace with your actual PostgreSQL connection URI
db = SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/api', methods=['POST'])
def create_person():
    data = request.get_json()
    name = data.get('name')

    if not name:
        return jsonify({"error": "Name is required"}), 400

    person = Person(name=name)
    db.session.add(person)
    db.session.commit()

    return jsonify({"message": "Person created successfully"}), 201

@app.route('/api/<int:user_id>', methods=['GET'])
def get_person(user_id):
    person = Person.query.get(user_id)

    if not person:
        return jsonify({"error": "Person not found"}), 404

    return jsonify({"id": person.id, "name": person.name})

@app.route('/api/<int:user_id>', methods=['PUT'])
def update_person(user_id):
    person = Person.query.get(user_id)

    if not person:
        return jsonify({"error": "Person not found"}), 404

    data = request.get_json()
    new_name = data.get('name')

    if not new_name:
        return jsonify({"error": "Name is required"}), 400

    person.name = new_name
    db.session.commit()

    return jsonify({"message": "Person updated successfully"})

@app.route('/api/<int:user_id>', methods=['DELETE'])
def delete_person(user_id):
    person = Person.query.get(user_id)

    if not person:
        return jsonify({"error": "Person not found"}), 404

    db.session.delete(person)
    db.session.commit()

    return jsonify({"message": "Person deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)
