from flask_login import login_user
from App.models import db, User, Staff, Customer, listing
from .game import create_game
from .user import create_customer, create_staff
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
    bob = create_staff('bob', 'bobpass')
    game1 = create_game('my game', 12324)
    game2 = create_game('my game2', 12325)
    game3 = create_game('my game3', 12326)
    list_game(bob.id, rob.id, game1.gameId, 'ok', 11)
    list_game(bob.id, rob.id, game2.gameId, 'good', 12)
    list_game(bob.id, rob.id, game3.gameId, 'new', 13)
    

