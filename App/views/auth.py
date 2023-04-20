from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify, flash, url_for
from flask_login import login_user, logout_user, current_user

auth_views = Blueprint('auth_views', __name__, template_folder='../templates')
from App.models import db, User
from App.controllers import login, user_required

@auth_views.route("/")
def login_page():
  if current_user.is_authenticated:
    logout_user()
  return render_template('login.html')

@auth_views.route('/signup', methods=['GET'])
def signup_page():
  return render_template('signup.html')

@auth_views.route('/login', methods=['POST'])
def login_action():
  data = request.form
  user = login(data['username'], data['password'])
  if user:  # check credentials
    flash('Logged in successfully.')  # send message to next page
    login_user(user)  # login the user
    return redirect('/home')  # redirect to main page if login successful
  else:
    flash('Invalid username or password')  # send message to next page
  return redirect(request.referrer)

@auth_views.route('/signup', methods=['POST'])
def signup_action():
  data = request.form  # get data from form submission
  newuser = User(username=data['username'],password=data['password'])  # create user object
  try:
    db.session.add(newuser)
    db.session.commit()  # save user
    #login_user(newuser)  # login the user
    flash('Account Created!')  # send message
    return redirect(url_for('auth_views.login_page'))  # redirect to homepage
  except Exception as e:  # attempted to insert a duplicate user
    db.session.rollback()
    flash("username or email already exists")  # error message
  return redirect(url_for('auth_views.signup_page'))

@auth_views.route('/logout', methods=['GET'])
@user_required
def logout_action():
    logout_user()
    return redirect('/')