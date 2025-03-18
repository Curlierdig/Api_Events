from flask import Blueprint, render_template, jsonify, current_app
from datetime import datetime
from mapkick.flask import Map
import requests

bp = Blueprint('views', __name__)
# Blueprint para la ruta raiz de la aplicación
@bp.route('/')
def index():
    api_get_event = "http://127.0.0.1:4000/api/events/featured"

    try:
        mapbox_token = current_app.config['MAPBOX_TOKEN']
        response = requests.get(api_get_event)
        response.raise_for_status()

        events = response.json()

        return render_template('index.html', events=events, mapbox_token=mapbox_token)
    
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

@bp.route('/events')
def show_events():
    api_get_event = "http://127.0.0.1:4000/api/events"
    
    try:
        response = requests.get(api_get_event)
        response.raise_for_status()

        events = response.json()

        for event in events:
            if isinstance(event["date"], str):
                event["date"] = datetime.strptime(event["date"], "%a, %d %b %Y %H:%M:%S %Z")

        return render_template('events.html', events=events)
    
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500
# Blueprint para la ruta de detalle de un evento
@bp.route('/event/<int:id>')
def show_event(id):
    api_get_event = f"http://127.0.0.1:4000/api/events/{id}"

    try:
        response = requests.get(api_get_event)
        response.raise_for_status()

        event = response.json()

        if isinstance(event["date"], str):
                event["date"] = datetime.strptime(event["date"], "%a, %d %b %Y %H:%M:%S %Z")

        map = Map([{'latitude': event["location"]["lat"], 'longitude': event["location"]["lng"], 'label': event["name"]}], zoom=14, controls=True)

        return render_template('event_detail.html', event=event,  map=map, mapbox_token=current_app.config["MAPBOX_ACCESS_TOKEN"])
    
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500