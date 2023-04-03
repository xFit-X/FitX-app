from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from flask_login import current_user

from App.controllers import customer_required

rental_views = Blueprint('rental_views', __name__, template_folder='../templates')

from App.controllers import get_outstanding_customer_rentals

@customer_required
@rental_views.route('/rentals', methods=['GET'])
def index_page():
    rentals = get_outstanding_customer_rentals(current_user.id)
    print(rentals, current_user.id)
    return render_template('rentals.html', rentals=rentals)