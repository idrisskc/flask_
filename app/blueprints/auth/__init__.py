from flask import Blueprint, render_template, url_for, redirect
from app.blueprints.auth.auth import user_auth_bp

auth_bp = Blueprint('auth',__name__)
auth_bp.register_blueprint(user_auth_bp, url_prefix= '/user')