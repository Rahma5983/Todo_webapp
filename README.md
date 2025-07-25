MY STYLISH TO DO LIST WEBAPPLICATION


A simple, yet stylish, web-based To-Do List application built with Flask, Python, and SQLite. This application allows users to manage their tasks through a clean and interactive web interface, with data persistence powered by a SQLite database.

Features
1.Add Tasks: Easily add new tasks to your list.

2.View Tasks: See all your tasks, clearly distinguishing between completed and incomplete items.

3.Mark as Complete/Incomplete: Toggle the completion status of any task.

4.Delete Tasks: Remove tasks from your list permanently.

5.Data Persistence: All tasks are stored in a SQLite database, so your list remains intact even after closing and reopening the application.

6.Responsive Design: The application's interface is designed to look good on various screen sizes.

7.Modern UI: Utilizes clean CSS for an attractive and user-friendly experience.

Technologies Used
1.Backend: Python (Flask framework)

2.Database: SQLite (managed by Flask-SQLAlchemy)

3.Frontend: HTML5, CSS3 (with Google Fonts for typography)

Usage
1.Add a Task: Type your task description into the input field at the top and click the "Add Task" button.

2.Mark/Unmark Task: Click the "Mark Complete" (or "Unmark") button next to a task to toggle its completion status.

3.Delete Task: Click the "Delete" button next to a task to remove it from the list.

Project Structure
# app.py: The main Flask application file, containing routes, database model, and application logic.

# templates/: Directory for HTML template files.

# index.html: The main page displaying the To-Do list and input form.

# static/: Directory for static assets like CSS.

# style.css: Contains all the styling rules for the web application.

requirements.txt: Lists all Python dependencies required for the project.

todo.db: The SQLite database file (automatically created on first run if it doesn't exist).

Feel free to contribute, fork, or modify this project!
