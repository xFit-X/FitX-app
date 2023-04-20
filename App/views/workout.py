from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify, flash
from flask_login import current_user

workout_views = Blueprint('workout_views', __name__, template_folder='../templates')
from App.controllers import (
    save_workout,
    get_all_workouts1,
    get_workout_by_id,
    user_required
)

@workout_views.route('/workout', methods=['POST'])
@user_required
def saveWorkout():
  data = request.form 
  pub = request.form.get('public') == 'on' 
  new_workout = save_workout(current_user.id, data["workoutId"],data["pname"],data["sets"], data["reps"], data["weight"], data["day"],pub)
  # workout = get_workout_by_id(new_workout.workoutId)
  flash('Successfully Saved' + " " + data["pname"])
  return redirect(request.referrer)


@workout_views.route('/workouts/<value>', methods=['GET'])
def workout_page(value):

    type_group = ["cardio", "plyometrics", "strength","stretching","strongman","powerlifting"]
    muscle_group  = ["abdominals", "biceps", "chest","glutes","quadriceps","lower_back","abductors","calves", "hamstrings"]
    difficulty_group = ["beginner", "intermediate", "expert"]
    muscle = None
    workout_type = None
    difficulty = None
    if value in muscle_group:
      muscle = value
    elif value in type_group:
      workout_type = value
    elif value in difficulty_group:
      difficulty = value
   
    w_days = {"Monday": "mon", "Tuesday": "tue", 
    "Wednesday": "wed", "Thursday": 
    "thu", "Friday": "fri", 
    "Saturday": "sat", "Sunday": "sun"}
    workouts = get_all_workouts1(muscle=muscle, workout_type=workout_type, difficulty=difficulty)    
    return render_template('workout.html', workouts=workouts, value=value.title(), w_days=w_days)
   