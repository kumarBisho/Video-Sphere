from .extensions import db, login_manager, bcrypt
from flask_login import UserMixin
from datetime import datetime
from urllib.parse import urlparse, parse_qs


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    videos = db.relationship('Video', backref='owner', lazy=True, cascade="all, delete-orphan")
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    
    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        
    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

class Video(db.Model):
    __tablename__ = 'videos'
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    duration = db.Column(db.String(64), nullable=False)
    url = db.Column(db.String(512), nullable=False)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    
    def to_dict(self):
        return {
            'user_id': self.user_id,
            'id': self.id,
            'title': self.title,
            'duration': self.duration,
            'url': self.url,
            'description': self.description,
            'created_at': self.created_at.isoformat(), # Convert datetime to ISO format string
            'updated_at': self.updated_at.isoformat()  # Convert datetime to ISO format string
        }
        
        
    @property
    def embed_url(self) -> str | None:
        """Return a proper YouTube embed URL for the video."""
        if not self.url:
            return None
        
        parsed_url = urlparse(self.url)
        query = parse_qs(parsed_url.query)
        
        video_id = query.get('v')
        if video_id:
            # Looping single video safely
            return f"https://www.youtube.com/embed/{video_id[0]}?playlist={video_id[0]}&loop=1"

        if 'youtu.be' in parsed_url.hostname:
            video_id = parsed_url.path.lstrip('/')
            return f"https://www.youtube.com/embed/{video_id}?playlist={video_id}&loop=1"

        return None