My Stylish To-Do List Web Application
A simple, yet stylish, web-based To-Do List application built with Flask, Python, and SQLite. This application allows users to manage their tasks through a clean and interactive web interface, with data persistence powered by a SQLite database.

Features
Add Tasks: Easily add new tasks to your list.

View Tasks: See all your tasks, clearly distinguishing between completed and incomplete items.

Mark as Complete/Incomplete: Toggle the completion status of any task.

Delete Tasks: Remove tasks from your list permanently.

Data Persistence: All tasks are stored in a SQLite database, so your list remains intact even after closing and reopening the application.

Responsive Design: The application's interface is designed to look good on various screen sizes.

Modern UI: Utilizes clean CSS for an attractive and user-friendly experience.

Technologies Used
Backend: Python (Flask framework)

Database: SQLite (managed by Flask-SQLAlchemy)

Frontend: HTML5, CSS3 (with Google Fonts for typography)

Setup and Installation
Follow these steps to get the To-Do List web application up and running on your local machine.

1. Clone the Repository (or create project structure)
If you're starting from scratch, create a project directory and the necessary subdirectories:

todo-webapp/
├── app.py
├── templates/
│   └── index.html
└── static/
    └── style.css
└── requirements.txt

2. Install Dependencies
Navigate to your project directory in the terminal and install the required Python packages using pip. It's highly recommended to use a virtual environment to manage your project's dependencies.

# Optional: Create a virtual environment (if you haven't already)
python -m venv .venv

# Activate the virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

# Install the required packages
pip install -r requirements.txt

The requirements.txt file should contain:

Flask
Flask-SQLAlchemy

3. Run the Application
Once the dependencies are installed and your virtual environment is active, you can run the Flask application:

python app.py

You should see output similar to this, indicating the server is running:

 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment.
Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit

4. Access the Web App
Open your web browser and navigate to the address provided in the terminal (usually http://127.0.0.1:5000).

You should now see your To-Do List application!

Usage
Add a Task: Type your task description into the input field at the top and click the "Add Task" button.

Mark/Unmark Task: Click the "Mark Complete" (or "Unmark") button next to a task to toggle its completion status.

Delete Task: Click the "Delete" button next to a task to remove it from the list.

Project Structure
app.py: The main Flask application file, containing routes, database model, and application logic.

templates/: Directory for HTML template files.

index.html: The main page displaying the To-Do list and input form.

static/: Directory for static assets like CSS.

style.css: Contains all the styling rules for the web application.

requirements.txt: Lists all Python dependencies required for the project.

todo.db: The SQLite database file (automatically created on first run if it doesn't exist).

Feel free to contribute, fork, or modify this project!
