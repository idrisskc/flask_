from flask import Blueprint, render_template, url_for, redirect

user_bp = Blueprint('user',__name__)

@user_bp.route('/')
def index():
    return '<h1>hello user</h1>'