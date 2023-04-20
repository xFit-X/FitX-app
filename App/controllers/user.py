from App.models import User
from App.database import db


def create_user(username, password):
    newuser = User(username=username, password=password)
    try:
        db.session.add(newuser)
        db.session.commit()
        return newuser
    except:
        return None

def get_user(id):
    return User.query.get(id)

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def get_all_users():
    return User.query.all()

def update_user(id, username):
    user = get_user(id)
    if user:
        user.username = username
        db.session.add(user)
        return db.session.commit()
    return None
