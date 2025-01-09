from . import db

class Course(db.Model):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(50), unique=True, nullable=False)
    details_of_course = db.Column(db.String(1000), unique=True, nullable=False)

    # Create a method to spit out a dictionary version of the course object for JSON serialization


    def to_dict(self):
        return {
            "id": self.id,
            "course_name": self.course_name,
            "details_of_course": self.details_of_course,
        }
