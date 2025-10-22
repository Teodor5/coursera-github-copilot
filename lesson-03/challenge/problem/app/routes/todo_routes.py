from flask import Blueprint, render_template, request, redirect, url_for
from app.services.todo_service import TodoService

bp = Blueprint('todos', __name__)

@bp.route('/')
def index():
    """Display the todo list."""
    todo_list = TodoService.get_all_todos()
    return render_template('base.html', todo_list=todo_list)

@bp.route("/add", methods=["POST"])
def add():
    """Add a new todo item."""
    title = request.form.get("title")
    TodoService.create_todo(title)
    return redirect(url_for("todos.index"))

@bp.route("/update/<int:todo_id>")
def update(todo_id):
    """Update the status of a todo item."""
    TodoService.update_todo_status(todo_id)
    return redirect(url_for("todos.index"))

@bp.route("/delete/<int:todo_id>")
def delete(todo_id):
    """Delete a todo item."""
    TodoService.delete_todo(todo_id)
    return redirect(url_for("todos.index"))