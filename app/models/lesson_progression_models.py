from . import db

class LessonProgression(db.Model):
    __tablename__ = 'lesson_progressions'

    id = db.Column(db.Integer, primary_key=True)
    progression_id = db.Column(db.Integer, nullable=False)
    lesson_id = db.Column(db.Integer, nullable=False)




    # Create a method to spit out a dictionary version of the course object for JSON serialization


    def to_dict(self):
        return {
            "id": self.id,
            "progression_id": self.progression_id,
            "lesson_id": self.lesson_id,

        }
