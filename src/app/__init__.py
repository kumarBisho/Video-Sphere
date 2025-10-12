from flask import Flask
from .config import config_by_name
from .extensions import db, migrate

def create_app(config_name: str='development')->Flask:
    app = Flask(__name__, static_folder='../static', template_folder='templates')
    app.config.from_object(config_by_name[config_name])
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    from .routes import main_bp
    from .api import api_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp, url_prefix='/api')
    
    return app
