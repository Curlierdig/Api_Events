from flask import Blueprint, jsonify, request
from app.models.eventsModel import EventModel

bp = Blueprint('api', __name__, url_prefix='/api')
# Aqui colocamos con blueprints las rutas de la API y las funciones que se encargan de manejarlas
# Blueprint para la ruta de eventos
@bp.route('/events', methods=['GET'])
def get_events():
    events = EventModel()
    return jsonify(events.get_events())
# Blueprint para la ruta de eventos filtrados
@bp.route('/events/filter', methods=['GET'])
def get_filtered_events():
    events = EventModel()
    try:
        start_date = request.args.get('fechaInicio')
        end_date = request.args.get('fechaFin')
        budget = request.args.get('presupuesto')
        type_id = request.args.getlist('tipo')
        match (budget, type_id):
            case ('', []):
                return jsonify(events.get_filtered_events(start_date, end_date))
            case ('', type_id):
                return jsonify(events.get_filtered_events(start_date, end_date, type_id))
            case (budget, []):
                return jsonify(events.get_filtered_events(start_date, end_date, type_id=None, budget=budget))
            case _:
                return jsonify(events.get_filtered_events(start_date, end_date, type_id, budget))
    except KeyError as e:
        return jsonify({'error': str(e)})
# Blueprint para la ruta de detalle de un evento
@bp.route('/events/<int:id>', methods=['GET'])
def get_event(id):
    events = EventModel()
    return jsonify(events.get_event_with_id(id))
# Blueprint para la ruta de eventos destacados
@bp.route('/events/featured', methods=['GET'])
def get_featured_events():
    events = EventModel()
    return jsonify(events.get_featured_events())