from . import db

class Review(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    review_title = db.Column(db.String(40), nullable=False)
    review = db.Column(db.String(500), nullable=False)


    # Create a method to spit out a dictionary version of the course object for JSON serialization


    def to_dict(self):
        return {
            "id": self.id,
            "review_title": self.review_title,
            "review": self.review,
        }
