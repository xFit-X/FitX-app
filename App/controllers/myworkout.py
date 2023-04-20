from App.models import UserWorkout, Workout, User, PersonalWorkout
from App.database import db
from App.config import config

import requests
import json


def save_workout(userId, workoutId,sets, reps, weight, day):
  w = Workout.query.filter_by(workoutId=workoutId).first()

  if weight is None or weight == "":
    if w.equipment not in ["other", "body_only", "body"]:
        weight = "10lbs"
    else:
        weight = "body"
    
  workout = UserWorkout(userId = userId, workoutId = workoutId ,sets = sets, reps=reps, weight = weight,day = day)
  user = User.query.filter_by(id=userId).first()
  db.session.add(workout)   
  user.workouts.append(workout)   
  db.session.commit()
  return workout

def save_personalworkout(userId,name, type, muscle, equipment, difficulty, sets, reps, day,weight,pub=False):

  workout = PersonalWorkout(userId=userId,name=name, muscle=muscle, equipment=equipment, difficulty=difficulty,
                  sets=sets,reps=reps,day=day,pub=pub,type = type, weight=weight)
  db.session.add(workout)
  db.session.commit()
  return workout

def edit_workout(uwId,userId,sets,reps,weight,day):
  workout = UserWorkout.query.filter_by(uwId = uwId, userId=userId).first()
  if workout:
    workout.sets = sets
    workout.reps = reps
    workout.weight = weight
    workout.day = day
    db.session.add(workout)
    db.session.commit()
    return workout
  return None

def edit_personalworkout(pwId,userId,name,sets,reps,weight,day):
  workout = PersonalWorkout.query.filter_by(pwid = pwId, userId=userId).first()
  if workout:
    workout.name= name
    workout.sets = sets
    workout.reps = reps
    workout.weight = weight
    workout.day = day
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

def delete_personalworkout(pwid,userId):
  workout = PersonalWorkout.query.filter_by(pwid = pwid, userId=userId).first()
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

def get_personalworkouts_by_day(userId,day):
  user = User.query.filter_by(id=userId).first()
  if user: 
      workout = PersonalWorkout.query.filter_by(day = day, userId=user.id).all()      
      return workout
  else:
    return None
    

def get_all_user_workouts():
  return UserWorkout.query.all()

def get_all_user_workouts2():
  return PersonalWorkout.query.all()

def get_user_workouts(userId):
  return UserWorkout.query.filter_by(userId=userId).all() 
  
 
    