from flask import Flask
from .config import config_by_name
from .extensions import db, migrate
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
    
    from .routes import main_bp
    from .api import api_bp
    
    # Register Blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp, url_prefix='/api')
    
    # Ensure tables exist (only for first deploy / SQLite fallback)
    with app.app_context():
        from .models import Video  # ensure models are imported
        db.create_all()  # creates tables if they don't exist
        db.session.commit()
    
    return app
