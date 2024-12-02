from app.database import db
from sqlalchemy import func
class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    description = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    likes = db.Column(db.Integer, server_default=0)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_onupdate=func.now())
    # Relationship to Event
    event = db.relationship('Event', backref='comments')


    def __repr__(self):
        return '<Location %r>' % self.name
