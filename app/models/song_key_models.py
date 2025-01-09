from . import db

class SongKey(db.Model):
    __tablename__ = 'song_keys'

    id = db.Column(db.Integer, primary_key=True)
    key_id = db.Column(db.Integer, nullable=False)
    song_id = db.Column(db.Integer, nullable=False)




    # Create a method to spit out a dictionary version of the course object for JSON serialization


    def to_dict(self):
        return {
            "id": self.id,
            "key_id": self.key_id,
            "song_id": self.song_id,

        }
