from App.models import UserWorkout, Workout, User
from App.database import db
from App.config import config

import requests
import json


def save_workout(userId, workoutId,name,sets, reps, weight, day,pub):
  w = Workout.query.filter_by(workoutId=workoutId).first()

  if weight is None or weight == "":
    if w.equipment not in ["other", "body_only", "body"]:
        weight = "10lbs"
    else:
        weight = "body"
  try: 
    workout = UserWorkout(userId = userId, workoutId = workoutId,name=name ,sets = sets, reps=reps, weight = weight,day = day,pub=pub)
    user = User.query.filter_by(id=userId).first()
    db.session.add(workout)   
    user.workouts.append(workout)   
    db.session.commit()
    return workout
  except:
    return None


def edit_workout(uwId,userId,name,sets,reps,weight,day,pub):
  workout = UserWorkout.query.filter_by(uwId = uwId, userId=userId).first()  
  if workout:
    if not name:
      name = workout.name
    if not sets:
      sets = workout.sets
    if not reps:
      reps = workout.reps
    if not weight: 
      weight =workout.weight
    if not day:
      day = workout.day 

    if pub is None:
      pub = workout.pub

    try: 
      workout.name = name
      workout.sets = sets
      workout.reps = reps
      workout.weight = weight
      workout.day = day
      workout.pub = pub
      db.session.add(workout)
      db.session.commit()
      return True
    except: 
      return None
  return None


def delete_workout(uwId,userId):
  workout = UserWorkout.query.filter_by(uwId = uwId, userId=userId).first()
  if workout:
    try:
      db.session.delete(workout)
      db.session.commit()
      return True
    except: 
      return None
  return None

def get_workouts_by_day(userId,day):
  user = User.query.filter_by(id=userId).first()
  if user: 
      workout = UserWorkout.query.filter_by(day = day, userId=user.id).all()      
      return workout
  else:
    return None

def get_all_user_workouts():
  return UserWorkout.query.all()

def get_user_workouts(userId):
  return UserWorkout.query.filter_by(userId=userId).all() 

def get_listing():
  return UserWorkout.query.filter_by(pub=True).all()

def save_listing_workout(uwId, userId):
  workout = UserWorkout.query.filter_by(uwId=uwId).first()
  if workout is None:
      return None
  if workout.userId == userId:
      return None
  else:
    try:
      new_workout = UserWorkout(name=workout.name,
                                workoutId=workout.workoutId,
                                sets=workout.sets,
                                reps=workout.reps,
                                weight=workout.weight,
                                day=workout.day,
                                userId=userId,
                                pub=False)
      db.session.add(new_workout)
      db.session.commit()
      return new_workout
    except:
      return None



  
 
    