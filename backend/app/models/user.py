from app.database import db
from sqlalchemy import func
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    username = db.Column(db.String, unique=True, nullable=False)
    hashed_password = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_onupdate=func.now())

  # Relationship to Profile
    profile = db.relationship('Profile', back_populates='user', uselist=False)
    # relationship to Event
    events = db.relationship('Event', backref='user')
    def __repr__(self):
        return '<User %r>' % self.username
