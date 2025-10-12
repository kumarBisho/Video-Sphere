from .extensions import db
from datetime import datetime

class Video(db.Model):
    __tablename__ = 'videos'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    duration = db.Column(db.String(64), nullable=False)
    url = db.Column(db.String(512), nullable=False)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'duration': self.duration,
            'url': self.url,
            'description': self.description,
            'created_at': self.created_at.isoformat(), # Convert datetime to ISO format string
            'updated_at': self.updated_at.isoformat()  # Convert datetime to ISO format string
        }