from app.database import db
from datetime import datetime
class Follower(db.Model):
    __tablenmae__ = 'followers'
    id = db.Column(db.Integer, primary_key=True)
    follower_id = db.Column(db.integer, ForiegnKey=('users.id'), nullable=False)
    following_id = db.Column(db.integer, ForiegnKey=('users.id'), nullable=False)
    created_at = db.Column(db.datetime, server_default=func.now())
