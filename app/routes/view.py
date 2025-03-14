from flask import Blueprint, render_template, jsonify, current_app
from mapkick.flask import Map
import requests

bp = Blueprint('views', __name__)
# Blueprint para la ruta raiz de la aplicación
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
# Blueprint para la ruta de detalle de un evento
@bp.route('/event/<int:id>')
def show_event(id):
    api_get_event = f"http://127.0.0.1:4000/api/events/{id}"

    try:
        response = requests.get(api_get_event)
        response.raise_for_status()

        event = response.json()
        
        # Crea un punto para el mapa con los datos del evento
        location_data = {
            'latitude': event["location"]["lat"], 
            'longitude': event["location"]["lng"],
            'title': event["name"],  # Asumiendo que el evento tiene un nombre
            'description': event["location"].get("address", "")  # Asumiendo que hay una dirección
        }
        
        # Crea el mapa con el punto
        map = Map([location_data])

        return render_template('event_detail.html', event=event, map=map, mapbox_token=current_app.config["MAPBOX_ACCESS_TOKEN"])
    
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500