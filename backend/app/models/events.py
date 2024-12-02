from app.database import db
from sqlalchemy import func

class Event(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    user_id =db.Column(db.Integer,ForiegnKey=('users.id'), nullable=False)
    name = db.Column(db.String, unique=True, nullable=False)
    location_id = db.Column(db.Integer, ForiegnKey=('locations.id'), nullable=False)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    event_time = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_onupdate=func.now())

    def __repr__(self):
        return '<Location %r>' % self.name
