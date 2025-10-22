from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app(config_class=Config):
    """Application factory function."""
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions
    db.init_app(app)

    # Register blueprints
    from app.routes.todo_routes import bp as todo_bp
    app.register_blueprint(todo_bp)

    # Create database tables
    with app.app_context():
        db.create_all()

    return app