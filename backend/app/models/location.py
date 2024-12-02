from app.database import db
from sqlalchemy import func
class Location(db.Model):
    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    description = db.Column(db.String)
    Created_by = db.Column(db.Integer, ForeignKey=('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_onupdate=func.now())

    def __repr__(self):
        return '<Location %r>' % self.name
