from flask import Blueprint, jsonify, request, abort
from .models import Video
from .extensions import db

api_bp = Blueprint('api', __name__)

@api_bp.route('/videos', methods = ['GET'])
def list_videos():
    videos = Video.query.order_by(Video.created_at.desc()).all()
    return jsonify([v.to_dict() for v in videos])

@api_bp.route('/videos/<int:id>', methods=['GET'])
def get_video(id):
    video = Video.query.get_or_404(id)
    return jsonify(video.to_dict())

@api_bp.route('/videos', methods=['POST'])
def create_video():
    data = request.get_json() or {}
    title = data.get('title')
    duration = data.get('duration')
    url = data.get('url')
    if not title or not duration or not url:
        return jsonify({'error': 'title, duration and url are required'}), 400
    video = Video(title=title.strip(), duration=duration.strip(), url=url.strip(), description=data.get('description').strip() if data.get('description') else None)
    db.session.add(video)
    db.session.commit()
    return jsonify(video.to_dict()), 201

@api_bp.route('/videos/<int:id>', methods=['PUT'])
def update_video(id):
    video = Video.query.get_or_404(id)
    data = request.get_json() or {}
    video.title = data.get('title', video.title).strip()
    video.duration = data.get('duration', video.duration).strip()
    video.url = data.get('url', video.url).strip()
    video.description = data.get('description', video.description).strip()
    db.session.commit()
    return jsonify(video.to_dict())

@api_bp.route('/videos/<int:id>', methods=['DELETE'])
def delete_video(id):
    video = Video.query.get_or_404(id)
    db.session.delete(video)
    db.session.commit()
    return jsonify({'result': 'Video deleted'}), 204