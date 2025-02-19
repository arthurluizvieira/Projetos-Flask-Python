from flask_sqlalchemy import SQLAlchemy

# Mova a inicialização do db para models.py
db = SQLAlchemy()

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'Task({self.title}, {self.description})'
