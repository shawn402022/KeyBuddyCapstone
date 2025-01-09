from . import db
from datetime import datetime

class SongProgression(db.Model):
    __tablename__ = 'song_progressions'

    id = db.Column(db.Integer, primary_key=True)
    lesson_id = db.Column(db.Integer, nullable=False)
    progression_id = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow,onupdate=datetime.utcnow)




    # Create a method to spit out a dictionary version of the course object for JSON serialization


    def to_dict(self):
        return {
            "id": self.id,
            "lesson_id": self.lesson_id,
            "progression_id": self.progression_id,


        }
