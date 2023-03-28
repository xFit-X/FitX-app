from flask import Blueprint, redirect, render_template, request, send_from_directory

index_views = Blueprint('index_views', __name__, template_folder='../templates')
from App.controllers import (get_all_listings)

@index_views.route('/', methods=['GET'])
def index_page():
    listings = get_all_listings()
    return render_template('index.html', listings=listings)