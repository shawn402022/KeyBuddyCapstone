from . import db
from datetime import datetime

class Chord(db.Model):
    __tablename__ = 'chords'

    id = db.Column(db.Integer, primary_key=True)
    chord_name = db.Column(db.String(50), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow,onupdate=datetime.utcnow)

    # Create a method to spit out a dictionary version of the course object for JSON serialization


    def to_dict(self):
        return {
            "id": self.id,
            "chord_name": self.chord_name,
        }
