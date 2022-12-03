from app import app, db
from .models import Task
from flask import request, make_response, jsonify


@app.route('/tasks/create/', methods=['POST'])
def create():
    data = request.get_json()
    new_task = Task(name=data['name'], description=data['description'])
    db.session.add(new_task)
    db.session.commit()
    return make_response(jsonify({"id": new_task.id}), 201)


