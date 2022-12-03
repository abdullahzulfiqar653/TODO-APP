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

@app.route('/tasks/')
def get():
    all_tasks = list()
    for task in Task.query.all():
        task_data = dict()
        task_data['id'] = task.id
        task_data['name'] = task.name
        task_data['description'] = task.description
        task_data['is_completed'] = task.is_completed
        all_tasks.append(task_data)

    return make_response(jsonify(all_tasks), 200)