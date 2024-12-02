from app.database import db
from sqlalchemy import func
class Profile(db.Model):
    __tablename__ = 'Profiles'

    id = db.Column(db.Integer, primary_key=True)
    # this will conect to the User table by user.id
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), unique=True, nullable=False)
    bio = db.Column(db.String)
    avatar_url = db.Column(db.String)

    # Relationship to User
    user = db.relationship('User', back_populates="profile")
    def __repr__(self):
        return '<Profile %r>' % self.username
