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
    allexercises = {
        "Muscle Group": {
            "abdominals": "https://i.imgur.com/ITkNaQF.jpg",
            "chest": "https://i.imgur.com/64E9dwe.jpg",
            "glutes": "https://i.imgur.com/akYHUfu.jpg",
            "biceps": "https://i.imgur.com/8CbLSfK.jpg",
            "quadriceps": "https://i.imgur.com/JkFAUR4.jpg",
            "lower_back": "https://i.imgur.com/XZ28MRQ.jpg",
            "abductors": "https://i.imgur.com/zSszIKa.jpg",
            "calves": "https://i.imgur.com/ae5g2vw.jpg",
            "hamstrings": "https://i.imgur.com/ITkNaQF.jpg"
        },
        
        "Difficulty": {
            "beginner": "https://i.imgur.com/mkmFc96.jpg",
            "intermediate": "https://i.imgur.com/yj68wj9.jpg",
            "expert": "https://i.imgur.com/ahtB3nB.jpg"
        },
        "Type": {
            "cardio": "https://i.imgur.com/KunmoF9.jpg",
            "plyometrics": "https://i.imgur.com/s7Ixets.jpg",
            "strength": "https://i.imgur.com/O8gPRcQ.jpg",
            "stretching": "https://i.imgur.com/DcqbcjV.jpg",
            "strongman": "https://i.imgur.com/itYgSYL.jpg",
            "powerlifting": "https://i.imgur.com/km1LYQY.jpg"
        }
    }

    return render_template('allworkouts.html',allexercises = allexercises)

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
