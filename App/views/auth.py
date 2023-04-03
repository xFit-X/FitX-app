from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from flask_login import login_user, logout_user

auth_views = Blueprint('auth_views', __name__, template_folder='../templates')
from App.models import Customer


@auth_views.route('/login', methods=['GET'])
def login_page():
    rentals = []
    sally = Customer.query.get(2)
    login_user(sally)
    return redirect(request.referrer)
    # return render_template('rentals.html', rentals=[])

@auth_views.route('/logout', methods=['GET'])
def logout_action():
    logout_user()
    return redirect('/')