from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify, json, flash
import requests
index_views = Blueprint('index_views', __name__, template_folder='../templates')
from App.controllers import (
    initialize,
    user_required
)



@index_views.route('/home', methods=['GET'])
@user_required
def index_page():
    return render_template('home.html')

@index_views.route('/init', methods=['GET'])
def init():
    initialize()
    return jsonify(message='db initialized!')

@index_views.route('/healthcheck', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})