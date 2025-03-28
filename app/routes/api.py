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
    """ Endpoint to filter the events by parameters given by arguments """
    events = EventModel()
    try:
        start_date = request.args.get('startDate')
        end_date = request.args.get('endDate')
        budget = request.args.get('presupuesto')
        type_id = request.args.getlist('tipo')

        # Convertir cadenas vacías a None
        start_date = start_date if start_date != '' else None
        end_date = end_date if end_date != '' else None
        budget = budget if budget != '' else None

        """ # Convertir budget a float si no es None
        if budget is not None:
            try:
                budget = float(budget)
            except ValueError:
                return jsonify({'error': 'Presupuesto no válido'}), 400 """

        # Determinar qué parámetros pasar al modelo
        args = {}
        if start_date is not None:
            args['start_date'] = start_date
        if end_date is not None:
            args['end_date'] = end_date
        if type_id:
            args['type_id'] = type_id
        if budget is not None:
            args['budget'] = budget

        filtered_events = events.get_filtered_events(**args)
        return jsonify(filtered_events)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
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