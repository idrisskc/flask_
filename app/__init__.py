from flask import Flask
# import os
# from dotenv import load_dotenv
# from flask_sqlalchemy import SQLAlchemy
# from app.extendsions import db, bootstrap, csrf

from app.blueprints.admin import admin_bp
from app.blueprints.auth import auth_bp
from app.blueprints.controllers import controller_bp
# from app.blueprints.services import service_bp
from app.config import Config
# from gevent import pywsgi
# import pymysql 

def create_app():
    app = Flask(__name__)
    # app.secret_key = Config.SECRET_KEY
    register_extension(app)
    register_blueprint(app)
    return app

def register_extension(app):
    #initialize db
    app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
    app.config['SECRET_KEY'] = Config.SECRET_KEY
    
def register_blueprint(app):
    app.register_blueprint(admin_bp, url_prefix= '/admin')
    app.register_blueprint(auth_bp, url_prefix= '/auth')
    app.register_blueprint(controller_bp, url_prefix= '/api')
    # app.register_blueprint(service_bp, url_prefix = '/services')
    # app.register_blueprint(middlewares_app, url_prefix = '/middleware')  

    
    
