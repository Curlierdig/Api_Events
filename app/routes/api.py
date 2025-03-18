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
    try:
        start_date = request.args.get('fechaInicio', default=None, type=str)
        end_date = request.args.get('fechaFin', default=None, type=str)
        budget = request.args.get('presupuesto', default=None, type=float)
        event_types = request.args.getlist('tipo')  # Usar getlist para múltiples valores
        
        # Lógica mejorada de filtrado
        filtered_events = EventModel.query
        
        if start_date and end_date:
            filtered_events = filtered_events.filter(
                EventModel.date >= start_date,
                EventModel.date <= end_date
            )
            
        if budget:
            filtered_events = filtered_events.filter(EventModel.budget <= budget)
            
        if event_types:
            filtered_events = filtered_events.filter(EventModel.type_id.in_(event_types))
        
        results = [event.to_dict() for event in filtered_events.all()]
        
        return jsonify(results)
    
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