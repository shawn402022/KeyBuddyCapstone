from . import db

class LessonSong(db.Model):
    __tablename__ = 'lesson_songs'

    id = db.Column(db.Integer, primary_key=True)
    song_id = db.Column(db.Integer, nullable=False)
    lesson_id = db.Column(db.Integer, nullable=False)




    # Create a method to spit out a dictionary version of the course object for JSON serialization


    def to_dict(self):
        return {
            "id": self.id,
            "song_id": self.song_id,
            "lesson_id": self.lesson_id,

        }
