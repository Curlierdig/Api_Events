from flask import Blueprint, jsonify, request
from app.models.eventsModel import EventModel

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/events', methods=['GET'])
def get_events():
    events = EventModel()
    return jsonify(events.get_events())

@bp.route('/events/filter', methods=['GET'])
def get_filtered_events():
    events = EventModel()
    start_date = request.args.get('fechaInicio')
    end_date = request.args.get('fechaFin')
    budget = request.args.get('presupuesto')
    type_id = request.args.getlist('tipo')

    return jsonify(events.get_filtered_events(start_date, end_date, type_id, budget))

@bp.route('/events/<int:id>', methods=['GET'])
def get_event(id):
    events = EventModel()
    return jsonify(events.get_event_with_id(id))

@bp.route('/events/featured', methods=['GET'])
def get_featured_events():
    events = EventModel()
    return jsonify(events.get_featured_events())