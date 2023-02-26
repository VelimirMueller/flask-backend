from src import db
from src import login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    registered_at = db.Column(db.DateTime)
    last_login = db.Column(db.DateTime)

    def set_hashed_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_hashed_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    @login.user_loader
    def load_user(id):
        return User.query.get(int(id))