"""Module contain all the views"""

from flask_api import status
from flask_restful import  Resource, reqparse

from app import db
from .models import Task

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('description')
parser.add_argument('is_completed')


class TaskView(Resource):
    """
    This view contain 2 methods only. get to fetch all tasks and post to
    create a task in todo list.
    """
    def get(self):
        """fetching all the tasks from Task table"""
        all_tasks = []
        for task in Task.query.all():
            task_data = {}
            task_data['id'] = task.id
            task_data['name'] = task.name
            task_data['is_completed'] = task.is_completed
            all_tasks.append(task_data)
        return all_tasks, status.HTTP_200_OK

    def post(self):
        """creating a task"""
        args = parser.parse_args()
        new_task = Task(name=args['name'], description=args['description'])
        db.session.add(new_task)
        db.session.commit()
        return {'id': new_task.id}, status.HTTP_201_CREATED


class RetrieveTaskView(Resource):
    """
    This View has 3 methods. by sending task_id you can retrieve, delete or
    update an task.
    """
    def get(self, task_id):
        """Retrieving specific task by id"""
        task = Task.query.filter_by(id=task_id).first_or_404()
        task_data = {}
        task_data['id'] = task.id
        task_data['name'] = task.name
        task_data['description'] = task.description
        task_data['is_completed'] = task.is_completed
        return task_data, status.HTTP_200_OK

    def delete(self, task_id):
        """deleting specific task by id"""
        Task.query.filter_by(id=task_id).first_or_404()
        Task.query.filter_by(id=task_id).delete()
        db.session.commit()
        return '', status.HTTP_204_NO_CONTENT

    def patch(self, task_id):
        """updating specific task by id"""
        task = Task.query.filter_by(id=task_id).first_or_404()
        args = parser.parse_args()
        name = args['name']
        description = args['description']
        is_completed = args['is_completed']
        task.name = name if name is not None else task.name
        task.description = description if description is not None else task.description
        task.is_completed = is_completed if is_completed is not None else task.is_completed
        db.session.commit()
        return {'id': task.id}, 200
