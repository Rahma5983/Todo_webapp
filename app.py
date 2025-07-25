from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# --- Flask App Setup ---
app = Flask(__name__)
# Configure SQLite database (tasks will be stored in 'todo.db' file)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# --- Database Model ---
# This defines the structure of your 'Task' table in the database
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Task {self.id}: {self.description}>'

# --- Routes (URLs your app responds to) ---

@app.route('/')
def index():
    """Displays the list of tasks."""
    tasks = Task.query.order_by(Task.id.desc()).all() # Get all tasks from DB
    return render_template('index.html', tasks=tasks) # Pass tasks to the template

@app.route('/add', methods=['POST'])
def add_task():
    """Adds a new task submitted via a form."""
    description = request.form.get('description') # Get data from the form
    if description:
        new_task = Task(description=description)
        db.session.add(new_task)
        db.session.commit() # Save to database
    return redirect(url_for('index')) # Redirect back to the home page

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    """Marks a task as complete."""
    # Corrected: Use Task.query.get_or_404
    task = Task.query.get_or_404(task_id) # Find task by ID
    task.completed = not task.completed # Toggle completion status
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    """Deletes a task."""
    # Corrected: Use Task.query.get_or_404
    task = Task.query.get_or_404(task_id) # Find task by ID
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))

# --- Run the App ---
if __name__ == '__main__':
    with app.app_context():
        db.create_all() # Create database tables if they don't exist
    app.run(debug=True) # debug=True allows auto-reloading and helpful error messages
