from app import app, db
from .models import Task
from flask import request, make_response, jsonify

@app.route('/')
def create_task():
    return make_response(jsonify("Home"), 200)