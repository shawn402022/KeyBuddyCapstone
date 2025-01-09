from . import db

class Progression(db.Model):
    __tablename__ = 'progressions'

    id = db.Column(db.Integer, primary_key=True)
    progression_name = db.Column(db.String(50), unique=True, nullable=False)


    # Create a method to spit out a dictionary version of the course object for JSON serialization


    def to_dict(self):
        return {
            "id": self.id,
            "progression_name": self.progression_name,
        }
