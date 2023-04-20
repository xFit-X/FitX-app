from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify, json, flash
import requests
from flask_login import current_user
myworkouts_views = Blueprint('myworkouts_views', __name__, template_folder='../templates')

from App.controllers import (
    get_workouts_by_day,
    edit_workout,
    delete_workout,
    user_required,
    get_all_workouts
)

#returns multiple workouts in each attribute so use a for loop to list
@myworkouts_views.route('/myworkouts', methods=['GET'])
@user_required
def myworkouts_page():

    w_workouts = ["mon", "tue","wed","thu","fri","sat" ,"sun"]
    week_workouts = [
        "Monday", 
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]

    workouts_dict = {}
    for day in w_workouts:
        workouts_dict[week_workouts[w_workouts.index(day)]] = get_workouts_by_day(current_user.id, day)
    workouts = get_all_workouts()

    w_days = {"Monday": "mon", "Tuesday": "tue", 
    "Wednesday": "wed", "Thursday": 
    "thu", "Friday": "fri", 
    "Saturday": "sat", "Sunday": "sun"}
    return render_template('myworkouts.html', days = workouts_dict, workouts = workouts, w_days=w_days)

@myworkouts_views.route('/myworkouts', methods=['POST'])
@user_required
def editWorkout():
    data = request.form
    pub = request.form.get('public') == 'on'
    new_workout = edit_workout(data["workoutId"],current_user.id, data["sets"], data["reps"], data["weight"], data["day"],pub)
    if(new_workout):
        flash("Successfully Edited")
        # workout = get_workout_by_id(new_workout.workoutId)
        return redirect(request.referrer)


#just does a flash and reloads the page to show the updated info
@myworkouts_views.route('/myworkouts/<int:uwid>', methods=['GET'])
@user_required
def deleteWorkout(uwid):
    if delete_workout(uwid,current_user.id):
        flash("Successfully Deleted")
        # workout = get_workout_by_id(new_workout.workoutId)
        return redirect(request.referrer)


