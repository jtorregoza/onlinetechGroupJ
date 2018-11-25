from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

db = SQLAlchemy()
ma = Marshmallow()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(20), nullable=False, unique=True)
    _password = db.Column('password', db.String(50), nullable=False)
    profile_image = db.Column(db.String(256), nullable=False, default='img.jpg')
    posts = db.relationship('Post', backref='illustrator', lazy=True)

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def set_password(self, value):
        self._password = generate_password_hash(value)

    def verify_password(self, given_password):
        return check_password_hash(self._password, given_password)

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title=db.Column(db.String(120), nullable=False)
    rating=db.Column(db.Integer, nullable=True, default=0)
    description=db.Column(db.String(500), nullable=True)
    date=db.Column(DateTime, nullable=False, default=datetime.now)
    image_file(db.String(256), nullable=False)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class UserSchema(ma.ModelSchema):
    class Meta():
        fields = ('id', 'username')

class PostSchema(ma.ModelSchema):
    class Meta():
        fields = ('title','image_file', 'description', 'rating', 'date')