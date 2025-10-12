from flask import Blueprint, render_template, redirect, url_for, flash, request
from .models import Video
from .extensions import db
from .forms import VideoForm

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    per_page = 10
    pagination = Video.query.order_by(Video.created_at.desc()).paginate(page=page, per_page=per_page, error_out=False)
    videos = pagination.items
    return render_template('index.html', videos=videos, pagination=pagination)

@main_bp.route('/video/<int:id>')
def view_video(id):
    video = Video.query.get_or_404(id)
    return render_template('view_video.html', video=video)

@main_bp.route('/videos/add', methods=['GET', 'POST'])
def add_video():
    form = VideoForm()
    if form.validate_on_submit():
        new_video = Video(
            title=form.title.data,
            description=form.description.data,
            url=form.url.data, 
            duration=form.duration.data
        )
        db.session.add(new_video)
        db.session.commit()
        flash('Video added successfully!', 'success')
        return redirect(url_for('main.index'))
    return render_template('add_video.html', form=form)

@main_bp.route('/videos/<int:id>/edit', methods=['GET', 'POST'])
def edit_video(id):
    video = Video.query.get_or_404(id)
    form = VideoForm(obj=video)
    if form.validate_on_submit():
        video.title = form.title.data
        video.description = form.description.data
        video.url = form.url.data
        video.duration = form.duration.data
        db.session.commit()
        flash('Video updated successfully!', 'success')
        return redirect(url_for('main.index'))
    return render_template('edit_video.html', form=form, video=video)

@main_bp.route('/videos/<int:id>/delete', methods=['POST'])
def delete_video(id):
    video = Video.query.get_or_404(id)
    db.session.delete(video)
    db.session.commit()
    flash('Video deleted successfully!', 'success')
    return redirect(url_for('main.index'))