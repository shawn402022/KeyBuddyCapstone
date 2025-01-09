from . import db

class Chord(db.Model):
    __tablename__ = 'chords'

    id = db.Column(db.Integer, primary_key=True)
    chord_name = db.Column(db.String(50), unique=True, nullable=False)


    # Create a method to spit out a dictionary version of the course object for JSON serialization


    def to_dict(self):
        return {
            "id": self.id,
            "chord_name": self.chord_name,
        }
