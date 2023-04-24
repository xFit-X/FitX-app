from flask_login import login_user, current_user, LoginManager
from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify, flash, url_for
from App.models import db, User
from .workout import cache_api_workouts
from .user import create_user
from functools import wraps

login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
     user =  User.query.get(user_id)
    if user:
        return user        


def login(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return user   
    return None

def initialize():
    db.drop_all()
    db.create_all()    
    bob = create_user('bob', 'bobpass')
    cache_api_workouts()
   

def user_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not current_user.is_authenticated or not isinstance(current_user, User):
            return redirect('/')
        return func(*args, **kwargs)
    return wrapper


