from . import db

class SongChord(db.Model):
    __tablename__ = 'song_chords'

    id = db.Column(db.Integer, primary_key=True)
    chord_id = db.Column(db.Integer)
    song_id = db.Column(db.Integer)




    # Create a method to spit out a dictionary version of the course object for JSON serialization


    def to_dict(self):
        return {
            "id": self.id,
            "chord_id": self.chord_id,
            "song_id": self.song_id,

        }
