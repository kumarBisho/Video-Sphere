from flask import Flask
from .config import config_by_name
from .extensions import db, migrate, login_manager, bcrypt
import os

def create_app(config_name: str='development')->Flask:
    app = Flask(__name__, static_folder='../static', template_folder='templates')
    app.config.from_object(config_by_name[config_name])
    
    # Use DATABASE_URL from environment if available (Render/PostgreSQL)
    database_url = os.getenv('DATABASE_URL')
    if database_url:
        app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    
    login_manager.login_view = 'auth.login'  # Redirect to login page if not authenticated
    login_manager.login_message_category = 'info'
    
    from .routes import main_bp
    from .api import api_bp
    from .auth.routes import auth_bp
    
    # Register Blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    
    # Ensure tables exist (only for first deploy / SQLite fallback)
    with app.app_context():
        from .models import Video, User  # ensure models are imported
        db.create_all()  # creates tables if they don't exist
        db.session.commit()
    
    return app
