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
    for day in week_workouts:
        workouts_dict[week_workouts[week_workouts.index(day)]] = get_workouts_by_day(current_user.id, day)
    workouts = get_all_workouts()

    w_days = {"Monday": "Monday", "Tuesday": "Tuesday", 
    "Wednesday": "Wednesday", "Thursday": 
    "Thursday", "Friday": "Friday", 
    "Saturday": "Saturday", "Sunday": "Sunday"}
    return render_template('myworkouts.html', days = workouts_dict, workouts = workouts, w_days=w_days)

@myworkouts_views.route('/myworkouts', methods=['POST'])
@user_required
def editWorkout():
    data = request.form
    if not data.get('pname'):
        pname = None
    else:
        pname = data.get('pname')

    if not data.get('sets'):
        sets = None
    else:
        sets = data.get('sets')

    if not data.get('reps'):
        reps = None
    else: 
        reps = data.get('reps')

    if not data.get('day'):
        day = None
    else:
        day = data.get('day')

    if not data.get('weight'):
        weight = None
    else:
        weight = data.get('weight')

    pub = None
    rempublic = request.form.get('public') == 'remove'
    addpublic = request.form.get('public') == 'add'

    if rempublic:
        pub = False
    elif addpublic:
        pub = True
        
    new_workout = edit_workout(data["workoutId"],current_user.id,pname, sets, reps, weight, day,pub)
    if(new_workout):
        flash("Successfully Edited")
        # workout = get_workout_by_id(new_workout.workoutId)
        return redirect(request.referrer)
    else:
        return redirect(request.referrer)


#just does a flash and reloads the page to show the updated info
@myworkouts_views.route('/myworkouts/<int:uwid>', methods=['GET'])
@user_required
def deleteWorkout(uwid):
    if delete_workout(uwid,current_user.id):
        flash("Successfully Deleted")
        # workout = get_workout_by_id(new_workout.workoutId)
        return redirect(request.referrer)


