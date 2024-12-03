from app.database import db
from sqlalchemy import func
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    username = db.Column(db.String, unique=True, nullable=False)
    hashed_password = db.Column(db.String, nullable=False)
    bio = db.Column(db.String, nullable=True)
    avatar_url = db.Column(db.String, nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, server_onupdate=db.func.now(), nullable=False)


    # relationship to Event
    events = db.relationship('Event', backref='users')
    locations = db.relationship('Location', backref="users")
    def __repr__(self):
        return '<User %r>' % self.username
