"""Contain routes to all imported views"""

from app import app
from flask_restful import Api

from .views import TaskView, RetrieveTaskView

api = Api(app)
api.add_resource(TaskView, '/tasks/')
api.add_resource(RetrieveTaskView, '/tasks/<task_id>/')
