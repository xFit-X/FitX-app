from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify

index_views = Blueprint('index_views', __name__, template_folder='../templates')
from App.controllers import (
    get_listing,
    get_all_listings,
    initialize,
)

@index_views.route('/', methods=['GET'])
@index_views.route('/<listing_id>', methods=['GET'])
def index_page(listing_id=None):
    listings = get_all_listings()
    selected = get_listing(listing_id) if listing_id else None
    return render_template('index.html', listings=listings, selected=selected)

@index_views.route('/init', methods=['GET'])
def init():
    initialize()
    return jsonify(message='db initialized!')

@index_views.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})