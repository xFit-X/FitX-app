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
    
  workout = UserWorkout(userId = userId, workoutId = workoutId,name=name ,sets = sets, reps=reps, weight = weight,day = day,pub=pub)
  user = User.query.filter_by(id=userId).first()
  db.session.add(workout)   
  user.workouts.append(workout)   
  db.session.commit()
  return workout


def edit_workout(uwId,userId,sets,reps,weight,day,pub):
  workout = UserWorkout.query.filter_by(uwId = uwId, userId=userId).first()
  if workout:
    workout.sets = sets
    workout.reps = reps
    workout.weight = weight
    workout.day = day
    workout.pub = pub
    db.session.add(workout)
    db.session.commit()
    return workout
  return None


def delete_workout(uwId,userId):
  workout = UserWorkout.query.filter_by(uwId = uwId, userId=userId).first()
  if workout:
    db.session.delete(workout)
    db.session.commit()
    return True
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
  
 
    