from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Task(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(255), nullable=False)

    description = db.Column(db.Text)

    priority = db.Column(db.String(20))

    due_date = db.Column(db.Date, nullable=False)

    status = db.Column(db.String(50), default="Pending")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "dueDate": str(self.due_date),
            "status": self.status
        }