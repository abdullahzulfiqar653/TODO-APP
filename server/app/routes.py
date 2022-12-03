from app import app, db
from .models import Task
from flask import request, make_response, jsonify
from flask_api import status

@app.route('/tasks/create/', methods=['POST'])
def create():
    data = request.get_json()
    new_task = Task(name=data['name'], description=data['description'])
    db.session.add(new_task)
    db.session.commit()
    return make_response(jsonify({"id": new_task.id}), status.HTTP_201_CREATED)

@app.route('/tasks/')
def get():
    all_tasks = list()
    for task in Task.query.all():
        task_data = dict()
        task_data['id'] = task.id
        task_data['name'] = task.name
        task_data['is_completed'] = task.is_completed
        all_tasks.append(task_data)
    return make_response(jsonify(all_tasks), status.HTTP_200_OK)

@app.route('/tasks/<id>/')
def retrieve(id):
    task = Task.query.filter_by(id=id).first_or_404()
    task_data = dict()
    task_data['id'] = task.id
    task_data['name'] = task.name
    task_data['description'] = task.description
    task_data['is_completed'] = task.is_completed
    return make_response(jsonify(task_data), status.HTTP_200_OK)

@app.route('/tasks/update/<id>/', methods=['PATCH'])
def update(id):
    task = Task.query.filter_by(id=id).first_or_404()
    data = request.get_json()
    task.name = data.get('name', None)
    task.description = data.get('description', task.description)
    task.is_completed = data.get('is_completed', task.is_completed)
    db.session.commit()
    return make_response('', status.HTTP_204_NO_CONTENT)


@app.route('/tasks/delete/<id>/', methods=['DELETE'])
def delete(id):
    Task.query.filter_by(id=id).first_or_404()
    Task.query.filter_by(id=id).delete()
    db.session.commit()
    return make_response('', status.HTTP_204_NO_CONTENT)