from .auth import auth_views
from .allworkouts import allworkouts_views
from .myworkouts import myworkouts_views
from .workout import workout_views
from .index import index_views

views = [
    workout_views,
    myworkouts_views,
    allworkouts_views,
    auth_views,
    index_views
]