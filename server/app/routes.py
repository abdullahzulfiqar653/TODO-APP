"""Contain routes to all imported views"""

from app import app
from .views import TaskView, RetrieveTaskView
from flask_restful import Api

api = Api(app)
api.add_resource(TaskView, '/tasks/')
api.add_resource(RetrieveTaskView, '/tasks/<task_id>/')
