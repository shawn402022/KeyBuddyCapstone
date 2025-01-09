from . import db

class SongProgression(db.Model):
    __tablename__ = 'song_progressions'

    id = db.Column(db.Integer, primary_key=True)
    lesson_id = db.Column(db.Integer, nullable=False)
    progression_id = db.Column(db.Integer, nullable=False)




    # Create a method to spit out a dictionary version of the course object for JSON serialization


    def to_dict(self):
        return {
            "id": self.id,
            "lesson_id": self.lesson_id,
            "progression_id": self.progression_id,


        }
