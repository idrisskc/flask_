from flask import Blueprint, render_template, url_for, redirect

user_auth_bp = Blueprint('user_auth',__name__)

@user_auth_bp.route('/')
def index():
    return '<h1>user_auth</h1>'