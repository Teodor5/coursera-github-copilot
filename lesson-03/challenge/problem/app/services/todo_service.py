from app import db
from app.models.todo import Todo

class TodoService:
    @staticmethod
    def get_all_todos():
        """Retrieve all todo items from the database."""
        return Todo.query.all()

    @staticmethod
    def create_todo(title):
        """Create a new todo item."""
        todo = Todo(title=title, complete=False)
        db.session.add(todo)
        db.session.commit()
        return todo

    @staticmethod
    def update_todo_status(todo_id):
        """Toggle the completion status of a todo item."""
        todo = Todo.query.filter_by(id=todo_id).first()
        if todo:
            todo.complete = not todo.complete
            db.session.commit()
        return todo

    @staticmethod
    def delete_todo(todo_id):
        """Delete a todo item."""
        todo = Todo.query.filter_by(id=todo_id).first()
        if todo:
            db.session.delete(todo)
            db.session.commit()
        return todo