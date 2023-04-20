from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify, json, flash
import requests
from flask_login import current_user
myworkouts_views = Blueprint('myworkouts_views', __name__, template_folder='../templates')

from App.controllers import (
    get_workouts_by_day,
    get_personalworkouts_by_day,
    edit_workout,
    edit_personalworkout,
    delete_workout,
    delete_personalworkout,
    user_required,
    get_all_workouts
)

#returns multiple workouts in each attribute so use a for loop to list
@myworkouts_views.route('/myworkouts', methods=['GET'])
@user_required
def myworkouts_page():
#     w_workouts = ["mon", "tue","wed","thu","fri","sat" ,"sun"]
#     mon = get_workouts_by_day(current_user.id,"mon")
#     tue = get_workouts_by_day(current_user.id,"tue")
#     wed = get_workouts_by_day(current_user.id,"wed")
#     thu = get_workouts_by_day(current_user.id,"thu")
#     fri = get_workouts_by_day(current_user.id,"fri")
#     sat = get_workouts_by_day(current_user.id,"sat")
#     sun = get_workouts_by_day(current_user.id,"sun")
#     workouts = get_all_workouts()
    

#     week_workouts = {
#     'Monday': (mon),
#     'Tuesday': (tue),
#     'Wednesday': (wed),
#     'Thursday': (thu),
#     'Friday': (fri),
#     'Saturday': (sat),
#     'Sunday': (sun)
# }
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

    personal_workouts_dict = {}
    for day in w_workouts:
        personal_workouts_dict[week_workouts[w_workouts.index(day)]] = get_personalworkouts_by_day(current_user.id, day)


    w_days = {"Monday": "mon", "Tuesday": "tue", 
    "Wednesday": "wed", "Thursday": 
    "thu", "Friday": "fri", 
    "Saturday": "sat", "Sunday": "sun"}
    return render_template('myworkouts.html', days = workouts_dict,pworkouts = personal_workouts_dict, workouts = workouts, w_days=w_days)

@myworkouts_views.route('/myworkouts', methods=['POST'])
@user_required
def editWorkout():
    data = request.form
    new_workout = edit_workout(data["workoutId"],current_user.id, data["sets"], data["reps"], data["weight"], data["day"])
    if(new_workout):
        flash("Successfully Edited")
        # workout = get_workout_by_id(new_workout.workoutId)
        return redirect(request.referrer)

@myworkouts_views.route('/myworkouts', methods=['POST'])
@user_required
def editPersonalWorkout():
    data = request.form
    new_workout = edit_personalworkout(data["pwid"],current_user.id, data["name"],data["sets"], data["reps"], data["weight"], data["day"])
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

@myworkouts_views.route('/personalworkouts/<int:pwid>', methods=['GET'])
@user_required
def deletePersonalWorkout(pwid):
    if delete_personalworkout(pwid,current_user.id):
        flash("Successfully Deleted")        
        return redirect(request.referrer)

@myworkouts_views.route('/createworkout' )
@user_required
def createWorkout_page():
    w_days = {"Monday": "mon", "Tuesday": "tue", 
    "Wednesday": "wed", "Thursday": 
    "thu", "Friday": "fri", 
    "Saturday": "sat", "Sunday": "sun"}
    return render_template('createworkout.html',w_days=w_days)