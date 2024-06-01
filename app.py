from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from youtube_api import fetch_video_views, VIDEO_IDS
import os

# Initialize the database object
db = SQLAlchemy()

# Define the Video model
class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    video_id = db.Column(db.String(12), unique=True, nullable=False)
    views = db.Column(db.Integer, nullable=False)

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/videos.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    @app.route('/')
    def index():
        videos = Video.query.all()
        return render_template('index.html', videos=videos)

    with app.app_context():
        db.create_all()
        video_data = fetch_video_views(VIDEO_IDS)
        for video in video_data:
            if not Video.query.filter_by(video_id=video['video_id']).first():
                new_video = Video(video_id=video['video_id'], views=int(video['views']))
                db.session.add(new_video)
        db.session.commit()

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

if __name__ != "__main__":
    app = create_app()
