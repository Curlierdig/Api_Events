from flask import Blueprint, render_template,current_app, request, redirect

bp = Blueprint('index', __name__)

@bp.route('/')
def index():
    return render_template('index.html', mapbox_token=current_app.config['MAPBOX_TOKEN'])