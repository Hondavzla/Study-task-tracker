# Import Flask for the web app and SQLAlchemy for database ORM support
from datetime import datetime

from flask import Flask
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


# Run setup and start the development server when this file is executed directly
if __name__ == "__main__":
    # Create database tables if they do not already exist
    with app.app_context():
        db.create_all()

    # Start Flask's built-in development server
    app.run(debug=True)
