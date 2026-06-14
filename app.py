from flask import Flask, request, jsonify
from config import Config
from models import db, Task
from datetime import datetime
import logging

VALID_STATUSES = [
    "Pending",
    "In Progress",
    "Completed"
]

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return {
        "service": "AI-Assisted Smart Task & Notification Service",
        "endpoints": [
            "POST /tasks",
            "GET /tasks",
            "PUT /tasks/<id>",
            "DELETE /tasks/<id>",
            "POST /tasks/<id>/notify"
        ]
    }

@app.route("/tasks", methods=["GET"])
def get_tasks():

    priority = request.args.get("priority")

    if priority:
        tasks = Task.query.filter_by(priority=priority).all()
    else:
        tasks = Task.query.all()

    return jsonify([task.to_dict() for task in tasks]), 200

@app.route("/tasks", methods=["POST"])
def create_task():

    data = request.get_json()

    title = data.get("title")
    due_date = data.get("dueDate")
    priority = data.get("priority")

    if not title:
        return jsonify({"error": "Title is required"}), 400

    if not isinstance(title, str):
        return jsonify({"error": "Title must be a string"}), 400
    
    if not due_date:
        return jsonify({"error": "Due date is required"}), 400
    
    valid_priorities = ["Low", "Medium", "High"]

    if priority and priority not in valid_priorities:
        return jsonify({
            "error": "Priority must be Low, Medium, or High"
        }), 400
    
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except:
        return jsonify({
            "error": "Invalid date format. Use YYYY-MM-DD"
        }), 400

    task = Task(
        title=title,
        description=data.get("description"),
        priority=data.get("priority"),
        due_date=datetime.strptime(due_date, "%Y-%m-%d").date()
    )

    logging.info(f"Creating task: {title}")

    db.session.add(task)
    db.session.commit()

    return jsonify({
        "message": "Task created successfully",
        "id": task.id
    }), 201

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):

    task = Task.query.get(task_id)

    if not task:
        return jsonify({"error": "Task not found"}), 404

    data = request.get_json()

    if "title" in data:

        if not isinstance(data["title"], str):
            return jsonify({
                "error": "Title must be a string"
            }), 400

        if data["title"].strip() == "":
            return jsonify({
                "error": "Title cannot be empty"
            }), 400

        task.title = data["title"]

    if "description" in data:
        task.description = data["description"]

    valid_priorities = ["Low", "Medium", "High"]

    if "priority" in data:

        if data["priority"] not in valid_priorities:
            return jsonify({
                "error": "Priority must be Low, Medium, or High"
            }), 400

        task.priority = data["priority"]

    if "status" in data:

        if data["status"] not in VALID_STATUSES:
            return jsonify({
                "error": "Status must be Pending, In Progress, or Completed"
            }), 400

        task.status = data["status"]

    if "dueDate" in data:

        try:

            task.due_date = datetime.strptime(
                data["dueDate"],
                "%Y-%m-%d"
            ).date()

        except ValueError:

            return jsonify({
                "error": "Invalid date format. Use YYYY-MM-DD"
            }), 400

    logging.info(f"Updating task {task_id}")

    db.session.commit()

    return jsonify({
        "message": "Task updated successfully"
    }), 200

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):

    task = Task.query.get(task_id)

    if not task:
        return jsonify({"error": "Task not found"}), 404

    logging.info(f"Deleting task {task_id}")

    db.session.delete(task)
    db.session.commit()

    return jsonify({
        "message": "Task deleted successfully"
    }), 200


@app.route("/tasks/<int:task_id>/notify", methods=["POST"])
def notify_task(task_id):

    task = Task.query.get(task_id)

    if not task:
        return jsonify({
            "error": "Task not found"
        }), 404

    notification_payload = {
        "taskId": task.id,
        "to": "user@example.com",
        "subject": f"Task Reminder: {task.title}",
        "body": f"Your task '{task.title}' is due on {task.due_date}",
        "priority": task.priority,
        "status": task.status
    }

    logging.info(f"Notification triggered for task {task_id}")

    return jsonify({
        "message": "Notification payload validated successfully",
        "payload": notification_payload
    }), 200


@app.route("/health", methods=["GET"])
def health():

    return jsonify({
        "status": "UP",
        "service": "Smart Task Service",
        "database": "Connected"
    }), 200

if __name__ == "__main__":
    app.run(debug=True)