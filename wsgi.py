import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.main import create_app
from App.models import ( User)
from App.controllers import *

# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')

#This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def initialize_db():
    initialize()
    print('database intialized')

# '''
# User Commands
# '''

# # Commands can be organized using groups

# # create a group, it would be the first argument of the comand
# # eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 

# # Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
def list_user_command():
    print(get_all_users())

@user_cli.command("login", help="Lists users in the database")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def login_user_command(username, password):
    res = login(username, password)
    if res:
        print(f'{username} logged in!')
    else:
        print('login unsuccessful!')



app.cli.add_command(user_cli) # add the group to the cli


# '''
# Workout Commands
# '''

workout_cli = AppGroup('workout', help='Workout object commands') 

    
@workout_cli.command("list_by_difficulty", help="Lists workouts by specified difficulty in the database")
@click.argument("query", default="beginner")
def list_workout_by_difficulty_command(query):
    print(get_all_workouts_by_diffculty(query))

@workout_cli.command("list_by_type", help="Lists workouts by specified type in the database")
@click.argument("query", default="cardio")
def list_workout_by_difficulty_command(query):
    print(get_all_workouts_by_type(query))

@workout_cli.command("list_by_muscle", help="Lists workouts by specified muscle in the database")
@click.argument("query", default="biceps")
def list_workout_by_difficulty_command(query):
    print(get_all_workouts_by_muscle(query))

@workout_cli.command("search", help="Get workout by specified name in the database")
@click.argument("name", default="push-ups")
def list_workout_by_difficulty_command(name):
    print(get_workout(name.title()))

@workout_cli.command("load", help="Loads workouts from the api into the database") 
def load_workout_command():
    workouts = cache_api_workouts()
    print(f"{len(workouts)} workouts loaded from API")

@workout_cli.command("list", help="Lists workouts in the database")
def list_workout_command():
    print(get_all_workouts())


app.cli.add_command(workout_cli)


# '''
# MyWorkout Commands
# '''

myworkout_cli = AppGroup('myworkout', help='User workouts commands') 

@myworkout_cli.command("save", help="Save workout for user into the database")
@click.argument("username", default="rob")
@click.argument("name", default="MyWorkout")
@click.argument("workoutid", default="53")
@click.argument("sets", default="3")
@click.argument("reps", default="8")
@click.argument("weight", default="25lbs")
@click.argument("day", default="mon")
@click.argument("pub", default=True)
def save_workout_command(username, workoutid,name, sets, reps, weight, day,pub):
  user = User.query.filter_by(username=username).first()
  if user:
    new_workout = save_workout(user.id, workoutid,name, sets, reps, weight, day,pub)
    workout = get_workout_by_id(new_workout.workoutId)
    print(f'Workout:{new_workout.uwId} {new_workout.name} {workout.name} {new_workout.sets} {new_workout.day} {new_workout.weight} {new_workout.pub}created!')
  else:
    print(f'{username} not found!')

@myworkout_cli.command("edit", help="Edit workout for user from the database")
@click.argument("username", default="bob")
@click.argument("uwid", default="4")
@click.argument("sets", default="3")
@click.argument("reps", default="10")
@click.argument("weight", default="body")
@click.argument("day", default="tue")
@click.argument("pub", default=False)
def edit_workout_command(username, uwid, sets, reps, weight, day,pub):
  user = User.query.filter_by(username=username).first()
  if user:
    new_workout = edit_workout(uwid,user.id,sets,reps,weight,day,pub)
    workout = get_workout_by_id(new_workout.workoutId)
    print(f'Workout:{new_workout.uwId} {workout.name} sets:{new_workout.sets} reps:{new_workout.reps} weight:{new_workout.weight} {new_workout.day} {new_workout.pub}edited!')
  else:
    print(f'{username} not found!')

@myworkout_cli.command("delete", help="Delete workout for user in the database")
@click.argument("username", default="bob")
@click.argument("uwid", default="4")
def delete_workout_command(username, uwid):
  user = User.query.filter_by(username=username).first()
  if user:
    if(delete_workout(uwid,user.id)):
        print(f'Workout deleted!')
    else:
        print(f'Invalid ID!')
  else:
    print(f'{username} not found!')

@myworkout_cli.command("list_by_day", help="List workouts for user by day in the database")
@click.argument("username", default="bob")
@click.argument("day", default="tue")
def list_workout_by_day_command(username, day):
  user = User.query.filter_by(username=username).first()
  if user:
    new_workout = get_workouts_by_day(user.id,day)
    for w in new_workout:
        workout = get_workout_by_id(w.workoutId)
        print(f'Workouts:{w.uwId} {workout.name} {w.day}')
  else:
    f'{username} not found!'


@myworkout_cli.command("list", help="Lists all user workouts in the database")
def list_all_user_workout_command():
    workout = get_all_user_workouts()
    if workout:
        print(workout)
    else:
        print(f'No workouts')

@myworkout_cli.command("user_workouts", help="Lists user workouts in the database")
@click.argument("username", default="rob")
def list_user_workout_command(username):
    user = User.query.filter_by(username=username).first()
    if user:
        workout = get_user_workouts(user.id)
        if workout:
            print(workout)
        else:
            print(f'No workouts')
    else:
        print(f'{username} not found!')


app.cli.add_command(myworkout_cli)
