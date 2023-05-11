from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login.user_loader # this is built in to our instance of our login manager instanced in our overall init
def load_user(user_id): # now we're going to get our user by our passed in ID, looking it up in table
    return User.query.get(user_id)

class User(UserMixin, db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    fav_book = db.Column(db.String)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    book_list = db.relationship('BookList', backref='reader', lazy=True)

    def __repr__(self):
        return f'User {self.username}'
    
    def commit(self):
        db.session.add(self)
        db.session.commit()

    def hash_password(self, password):
        return generate_password_hash(password)
    
    def check_password(self, password_input):
        return check_password_hash(self.password, password_input)
    
    def get_id(self): # this gets called automatically by flask_login when needed
        return str(self.user_id)

class BookList(db.Model):
    book_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    title = db.Column(db.String)
    author = db.Column(db.String)
    review = db.Column(db.String)

    def __repr__(self):
        return f'Book review for {self.title}'
    
    def commit(self):
        db.session.add(self)
        db.session.commit()