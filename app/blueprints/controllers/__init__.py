from flask import Blueprint, render_template, url_for, redirect
from app.blueprints.controllers.userController import user_controller_bp

controller_bp = Blueprint('controller',__name__)
controller_bp.register_blueprint(user_controller_bp, url_prefix='/user')
