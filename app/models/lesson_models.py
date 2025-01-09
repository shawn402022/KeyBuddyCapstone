from . import db
from datetime import datetime

class Lesson(db.Model):
    __tablename__ = 'lessons'

    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer,)
    name = db.Column(db.String(255), unique=True, nullable=False)
    type = db.Column(db.String(255), nullable=False)
    key = db.Column(db.String(255), unique=True, nullable=False)
    pulls_to = db.Column(db.String(100), nullable=False)
    pulls_from = db.Column(db.String(40), nullable=False)
    songs = db.Column(db.String(40), nullable=False)
    chords = db.Column(db.String(40), nullable=False)
    progressions = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow,onupdate=datetime.utcnow)


    # Create a method to spit out a dictionary version of the course object for JSON serialization


    def to_dict(self):
        return {
            "id": self.id,
            "course_id": self.course_id,
            "name": self.name,
            "type": self.type,
            "key": self.key,
            "pulls_to": self.pulls_to,
        }
