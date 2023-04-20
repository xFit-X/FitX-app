from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify, json, flash
import requests
from flask_login import current_user
allworkouts_views = Blueprint('allworkouts_views', __name__, template_folder='../templates')
from App.controllers import (
    get_workout,
    user_required,
    get_listing,
    get_all_workouts,
    save_listing_workout
)

@allworkouts_views.route('/allworkouts', methods=['GET'])
@user_required
def allworkouts_page():
    return render_template('allworkouts.html')

@allworkouts_views.route('/listing', methods=['GET'])
@user_required
def listing_page():
    workouts = get_all_workouts()
    listing = get_listing()
    return render_template('listing.html',listing=listing,workouts=workouts)

@allworkouts_views.route('/savelisting/<int:uwId>', methods=['GET'])
@user_required
def listing_action(uwId):
    workout = save_listing_workout(uwId,current_user.id)    
    if workout:
        flash('Successfully Saved' + " " + workout.name)
    else:
        flash('Already Saved')
    return redirect(request.referrer)

#returns multiple workouts
@allworkouts_views.route('/search', methods=['GET'])
@user_required
def searchWorkouts_page():
    query = request.args.get('query')
    workouts = get_workout(query)
    return render_template('search.html', workouts=workouts, search=query) 
