from . import db
from datetime import datetime

class LessonKey(db.Model):
    __tablename__ = 'lesson_keys'

    id = db.Column(db.Integer, primary_key=True)
    key_id = db.Column(db.Integer, nullable=False)
    lesson_id = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow,onupdate=datetime.utcnow)




    # Create a method to spit out a dictionary version of the course object for JSON serialization


    def to_dict(self):
        return {
            "id": self.id,
            "key_id": self.key_id,
            "lesson_id": self.lesson_id,

        }
