from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    video_id = db.Column(db.String(12), unique=True, nullable=False)
    views = db.Column(db.Integer, nullable=False)
