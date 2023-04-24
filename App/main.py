import os
from flask import Flask
from flask_login import LoginManager, current_user
from flask_uploads import DOCUMENTS, IMAGES, TEXT, UploadSet, configure_uploads
from flask_cors import CORS
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from datetime import timedelta

from App.database import init_db
from App.views import views
from App.config import config
from App.models import User


def add_views(app):
    for view in views:
        app.register_blueprint(view)


def configure_app(app, config):
    for key, value in config.items():
        app.config[key] = config[key]

def create_app(config_overrides={}):
    app = Flask(__name__, static_url_path='/static')
    CORS(app)
    configure_app(app, config)
    configure_app(app, config_overrides)
    # login_manager = LoginManager()
    # login_manager.init_app(app)
    photos = UploadSet('photos', TEXT + DOCUMENTS + IMAGES)
    configure_uploads(app, photos)
    add_views(app)
    init_db(app)
    app.app_context().push()

    # @login_manager.user_loader
    # def load_user(user_id):
    #     user =  User.query.get(user_id)
    #     if user:
    #         return user        

    return app

