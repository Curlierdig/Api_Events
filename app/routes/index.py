from flask import Blueprint, render_template, request, redirect

bp = Blueprint('index', __name__)

@bp.route('/')
def index():
    return render_template('index.html')