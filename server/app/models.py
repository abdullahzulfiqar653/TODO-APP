"""module contain DB Models"""

from app import db


class Task(db.Model):
    """Model defining attributes related to Task"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.Text)
    is_completed = db.Column(db.Boolean, default=False)
