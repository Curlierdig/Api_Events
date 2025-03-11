from flask import Blueprint, render_template, jsonify, current_app
from mapkick.flask import Map
import requests

bp = Blueprint('views', __name__)

@bp.route('/')
def index():
    api_get_event = "http://127.0.0.1:4000/api/events/featured"

    try:
        response = requests.get(api_get_event)
        response.raise_for_status()

        events = response.json()

        return render_template('index.html', events=events)
    
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

@bp.route('/event/<int:id>')
def show_event(id):
    api_get_event = f"http://127.0.0.1:4000/api/events/{id}"

    try:
        response = requests.get(api_get_event)
        response.raise_for_status()

        event = response.json()

        map = Map([{'latitude': event["location"]["lat"], 'longitude': event["location"]["lng"]}])

        return render_template('event_detail.html', event=event, map=map, mapbox_token=current_app.config["MAPBOX_ACCESS_TOKEN"])
    
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500