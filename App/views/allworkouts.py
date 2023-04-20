from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify, json, flash
import requests
allworkouts_views = Blueprint('allworkouts_views', __name__, template_folder='../templates')
from App.controllers import (
    get_workout,
    user_required
)

@allworkouts_views.route('/allworkouts', methods=['GET'])
@user_required
def allworkouts_page():
    return render_template('allworkouts.html')

#returns multiple workouts
@allworkouts_views.route('/search', methods=['GET'])
@user_required
def searchWorkouts_page():
    query = request.args.get('query')
    workouts = get_workout(query)
    return render_template('search.html', workouts=workouts, search=query) 
