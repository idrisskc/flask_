from flask import Blueprint, render_template, url_for, redirect

user_controller_bp = Blueprint('userController', __name__)
@user_controller_bp.route('/')
def index():
    return '<h1>user_controller</h1>'