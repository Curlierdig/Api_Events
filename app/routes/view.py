from flask import Blueprint, render_template, jsonify, current_app, request
from datetime import datetime
from mapkick.flask import Map
import requests
from app.models.eventsModel import EventModel

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

        return render_template('event_detail.html', event=event, map=map, mapbox_token=current_app.config["MAPBOX_ACCESS_TOKEN"])
    
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500
    
""" @bp.route('/api/events/filter', methods=['GET'])
def filter_events():
    # Obtener parámetros usando el objeto request de Flask
    start_date_str = request.args.get('start_date')
    end_date_str = request.args.get('end_date')
    type_ids = request.args.getlist('type_id[]')  # Para múltiples valores
    budget_str = request.args.get('budget')

    # Conversión de fechas con manejo de múltiples formatos
    start_date = None
    end_date = None
    try:
        if start_date_str:
            # Intentar con formato MM/DD/YYYY
            try:
                start_date = datetime.strptime(start_date_str, '%m/%d/%Y').date()
            except ValueError:
                # Si falla, intentar con formato YYYY-MM-DD
                start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
        
        if end_date_str:
            # Intentar con formato MM/DD/YYYY
            try:
                end_date = datetime.strptime(end_date_str, '%m/%d/%Y').date()
            except ValueError:
                # Si falla, intentar con formato YYYY-MM-DD
                end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
    
    except (ValueError, TypeError) as e:
        return jsonify({
            "error": f"Formato de fecha inválido: {str(e)}",
            "received_start_date": start_date_str,
            "received_end_date": end_date_str
        }), 400

    # Conversión de presupuesto
    budget = None
    if budget_str:
        try:
            budget = float(budget_str)
        except ValueError:
            return jsonify({"error": "El presupuesto debe ser un número válido"}), 400

    # Conversión de type_ids
    # Asegurarse de que type_ids sean enteros
    if type_ids:
        try:
            type_ids = [int(t) for t in type_ids]
        except ValueError:
            return jsonify({"error": "Los IDs deben ser números enteros"}), 400

    try:
        # Crear una instancia de EventModel
        event_manager = EventModel()
        
        # Obtener eventos filtrados
        filtered_events = event_manager.get_filtered_events(
            start_date=start_date,
            end_date=end_date,
            id=type_ids[0] if type_ids else None,  # Pasamos el primer id o None
            budget=budget
        )
        
        # Convertir eventos a formato JSON
        events_json = []
        for event in filtered_events:
            event_dict = dict(event)
            # Convertir datetime si es necesario
            if isinstance(event_dict.get('date'), datetime):
                event_dict['date'] = event_dict['date'].strftime("%a, %d %b %Y %H:%M:%S %Z")
            events_json.append(event_dict)
        
        return jsonify(events_json)
    
    except Exception as e:
        return jsonify({
            "error": str(e),
            "start_date": start_date,
            "end_date": end_date,
            "type_ids": type_ids,
            "budget": budget
        }), 500 """