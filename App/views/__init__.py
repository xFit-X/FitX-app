from .rental import rental_views
from .index import index_views
from .auth import auth_views
# from .game import game_views
# from .listing import listing_views
# from .payment import payment_views

views = [
    index_views,
    rental_views,
    auth_views
]