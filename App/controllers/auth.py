from flask_login import login_user, current_user
from App.models import db, User, Staff, Customer, listing
from .game import create_game, cache_api_games
from .user import create_customer, create_staff
from .rental import create_rental
from functools import wraps
from .listing import list_game

def login(username, password):
    staff = Staff.query.filter_by(username=username).first()
    if staff and staff.check_password(password):
        return staff
    customer = Customer.query.filter_by(username=username).first()
    if customer and customer.check_password(password):
        return customer
    return None

def initialize():
    db.drop_all()
    db.create_all()
    rob = create_customer('rob', 'robpass')
    sally = create_customer('sally', 'sallypass')
    bob = create_staff('bob', 'bobpass')
    cache_api_games()
    listing1 =  list_game(bob.id, rob.id, 23, 'ok', 11)
    list_game(bob.id, rob.id, 100, 'good', 12)
    list_game(bob.id, rob.id, 57, 'new', 13)
    rental = create_rental(sally.id, listing1.listingId)
    print(rental)

def customer_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not current_user.is_authenticated or not isinstance(current_user, Customer):
            return "Unauthorized", 401
        return func(*args, **kwargs)
    return wrapper

def staff_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not current_user.is_authenticated or not isinstance(current_user, Staff):
            return "Unauthorized", 401
        return func(*args, **kwargs)
    return wrapper

