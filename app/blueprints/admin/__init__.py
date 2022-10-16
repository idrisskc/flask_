from flask import Blueprint, render_template, url_for, redirect

# from app.extendsions import db
# from app.models import User
from app.blueprints.admin.user import user_bp

admin_bp = Blueprint('admin',__name__)
admin_bp.register_blueprint(user_bp, url_prefix='/user')
 
