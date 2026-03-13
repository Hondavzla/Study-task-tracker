# Import Flask for the web app and SQLAlchemy for database ORM support
from datetime import datetime

from flask import Flask, abort, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

# Create the Flask application instance
app = Flask(__name__)

# Configure SQLite database location (saved in instance/tasks.db)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"

# Disable event system tracking to avoid extra overhead/warnings
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Connect SQLAlchemy to this Flask app
db = SQLAlchemy(app)


# Define the Task table structure using a model class
class Task(db.Model):
    # Unique ID for each task (primary key, auto-incremented)
    id = db.Column(db.Integer, primary_key=True)

    # Short task title (required, max 200 characters)
    title = db.Column(db.String(200), nullable=False)

    # Course name the task belongs to (required, max 100 characters)
    course = db.Column(db.String(100), nullable=False)

    # Due date stored as a simple string (required, max 20 characters)
    due_date = db.Column(db.String(20), nullable=False)

    # Optional longer details about the task
    description = db.Column(db.Text, nullable=True)

    # Completion status (required, defaults to False)
    completed = db.Column(db.Boolean, nullable=False, default=False)

    # Timestamp set automatically when a task is created (UTC time)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    # Helpful string representation when printing task objects
    def __repr__(self):
        return f"<Task '{self.title}'>"


# Home page route: show all tasks ordered by due date (earliest first)
@app.route("/")
def index():
    tasks = Task.query.order_by(Task.due_date.asc()).all()
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["GET", "POST"])
def add_task():
    # Show the empty add-task form when the user visits the page
    if request.method == "GET":
        return render_template("add_task.html")

    # Read submitted form values safely (returns None if a key is missing)
    title = request.form.get("title")
    course = request.form.get("course")
    due_date = request.form.get("due_date")
    description = request.form.get("description")

    # Create a new Task object (completed defaults to False in the model)
    new_task = Task(
        title=title,
        course=course,
        due_date=due_date,
        description=description,
    )

    # Save the new task to the database
    db.session.add(new_task)
    db.session.commit()

    # Send the user back to the home page after saving
    return redirect(url_for("index"))


@app.route("/edit/<int:task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    # Fetch the task by primary key
    task = db.session.get(Task, task_id)

    # Return 404 if the task does not exist
    if task is None:
        abort(404)

    # Show the edit form pre-filled with current task data
    if request.method == "GET":
        return render_template("edit_task.html", task=task)

    # Read submitted form values safely
    title = request.form.get("title")
    course = request.form.get("course")
    due_date = request.form.get("due_date")
    description = request.form.get("description")

    # Update fields on the existing task object
    task.title = title
    task.course = course
    task.due_date = due_date
    task.description = description

    # Commit changes to save updates
    db.session.commit()

    # Return to the index page after saving
    return redirect(url_for("index"))


@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    # Fetch the task by primary key
    task = db.session.get(Task, task_id)

    # Return 404 if the task does not exist
    if task is None:
        abort(404)

    # Delete the task from the database session
    db.session.delete(task)

    # Commit the transaction to save changes
    db.session.commit()

    # Return to the index page after deleting
    return redirect(url_for("index"))


@app.route("/toggle/<int:task_id>", methods=["POST"])
def toggle_task(task_id):
    # Fetch the task by primary key
    task = db.session.get(Task, task_id)

    # Return 404 if the task does not exist
    if task is None:
        abort(404)

    # Toggle completion status (True becomes False, False becomes True)
    task.completed = not task.completed

    # Commit the transaction to save the updated status
    db.session.commit()

    # Return to the index page after toggling
    return redirect(url_for("index"))


# Run setup and start the development server when this file is executed directly
if __name__ == "__main__":
    # Create database tables if they do not already exist
    with app.app_context():
        db.create_all()

    # Start Flask's built-in development server
    app.run(debug=True)
