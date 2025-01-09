from . import db

class Song(db.Model):
    __tablename__ = 'songs'

    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(40), nullable=False)
    song = db.Column(db.String(100), nullable=False)
    artist = db.Column(db.String(40), nullable=False)
    chords_used = db.Column(db.String(40), nullable=False)
    progression_used = db.Column(db.String(40), nullable=False)


    # Create a method to spit out a dictionary version of the course object for JSON serialization


    def to_dict(self):
        return {
            "id": self.id,
            "key": self.key,
            "song": self.song,
            "artist": self.artist,
            "chords_used": self.chords_used,
            "progression_used": self.progression_used,
        }
