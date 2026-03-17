# Study Task Tracker
A full-stack web app for students to manage coursework tasks, due dates, and completion status in one place.

## Live Demo 🚀
https://study-task-tracker-17mz.onrender.com

## Screenshots 🖼️
(screenshots coming soon)

## Features
- View all tasks in a responsive card grid
- Add a new task with title, course, due date, and optional description
- Edit any existing task
- Delete a task
- Mark tasks complete or incomplete with a toggle
- Expand/collapse task descriptions using an accordion
- Dynamic days-remaining calculation for each task
- Automatic overdue detection with red status badges
- Color-coded course badges by subject
- Stats banner showing tasks remaining, overdue count, and completed count
- Responsive layout for desktop, tablet, and mobile

## Tech Stack
- **Backend:** Python, Flask
- **Database:** SQLite, Flask-SQLAlchemy
- **Frontend:** HTML, CSS, vanilla JavaScript
- **Version Control:** Git, GitHub
- **Deployment:** Render

## Project Structure
```text
study-task-tracker/
├── app.py                 # Flask app, routes, and Task model logic
├── requirements.txt       # Python dependency list for this project
├── README.md              # Project overview, setup steps, and notes
├── static/
│   ├── style.css          # App styling, layout, and responsive rules
│   └── script.js          # Frontend JS (accordion and UI interactions)
├── templates/
│   ├── base.html          # Shared base layout (navbar, main wrapper, footer)
│   ├── index.html         # Home page with task cards and actions
│   ├── add_task.html      # Form page to create a new task
│   └── edit_task.html     # Form page to update an existing task
└── instance/
    └── tasks.db           # Local SQLite database file
```

## Getting Started
1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/study-task-tracker.git
   cd study-task-tracker
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment**
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - Windows (PowerShell):
     ```powershell
     .\\venv\\Scripts\\Activate.ps1
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the app**
   ```bash
   python app.py
   ```

6. **Open in your browser**
   ```
   http://127.0.0.1:5000
   ```

## What I Learned
- I learned how to build a full-stack app from scratch and connect frontend pages to backend logic.
- I got more comfortable with Flask routes, request handling, and Jinja2 template rendering.
- I practiced database design with SQLite and implemented full CRUD operations.
- I improved my Git and GitHub workflow by making structured commits while building features step by step.
- I learned how responsive CSS changes the user experience across desktop, tablet, and mobile.
- I got better at debugging by breaking problems into small parts and testing one change at a time.

## Future Improvements
- Add user authentication so each student has a private task dashboard
- Add filter and sort options by course, due date, and completion status
- Add due date reminder notifications
- Add a dark mode toggle

Built by Ricardo salcedo — CS Student
