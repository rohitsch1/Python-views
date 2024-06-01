
from flask import render_template
from app import app
from models import Video

@app.route('/')
def index():
    videos = Video.query.all()
    return render_template('index.html', videos=videos)
