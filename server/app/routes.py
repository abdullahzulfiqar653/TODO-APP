from app import api
from .views import TaskView, RetrieveTaskView

api.add_resource(TaskView, '/tasks/')
api.add_resource(RetrieveTaskView, '/tasks/<task_id>/')