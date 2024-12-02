from app.database import db

class Profiles(db.Model):
    __tablename__ = 'Profiles'

    id = db.Column(db.Integer, primary_key=True)
    # this will conect to the User table by user.id
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), unique=True, nullable=False)
    bio= db.Column(db.String)
    avatar_url = db.Column(db.String)
    username = db.Column(db.String, unique=True,nullable=False)
    password = db.Column(db.String, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
