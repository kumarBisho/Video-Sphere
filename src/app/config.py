import os
from dotenv import load_dotenv

load_dotenv()

basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'change-me')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', f'sqlite:///{os.path.join(basedir, "youtube_manager.db")}')    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
class DevelopmentConfig(Config):
    DEBUG = True
    
class ProductionConfig(Config):
    DEBUG = False
    
config_by_name = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}