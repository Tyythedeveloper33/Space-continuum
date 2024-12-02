from app.database import db

class Location(db.Model):
    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    description = db.Column(db.String)
    Created_by = db.Column(db.Integer, ForeignKey=('profiles.id'), nullable=False)

    def __repr__(self):
        return '<Location %r>' % self.name
