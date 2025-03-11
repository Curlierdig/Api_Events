from datetime import timedelta, date
from app.utils.db_utils import get_cursor, close_cursor

class EventModel:
    def __init__(self):
        self.events = ()
        self.cur = get_cursor()
        self.location = ()
        self.organizer = ()
        self.type = ()

    def get_location_by_id(self, id_location):
        self.cur.execute("SELECT * FROM tlocations WHERE id = %s", (id_location,))
        self.location = self.cur.fetchone()
        return self.location
    
    def get_organizer_by_id(self, id_organizer):
        self.cur.execute("SELECT * FROM torganizers WHERE id = %s", (id_organizer,))
        self.organizer = self.cur.fetchone()
        return self.organizer
    
    def get_type_by_id(self, id_type):
        self.cur.execute("SELECT * FROM tevent_types WHERE id = %s", (id_type,))
        self.type = self.cur.fetchone()
        return self.type

    def get_details(self, events_data):
        if isinstance(events_data, dict):
            events_data["location"] = self.get_location_by_id(events_data["location_id"])
            events_data["organizer"] = self.get_organizer_by_id(events_data["organizer_id"])
            events_data["type"] = self.get_type_by_id(events_data["type_id"])

            return events_data
        else:
            events_with_details = []

            for event in events_data:
                event_copy = dict(event)

                event_copy["location"] = self.get_location_by_id(event["location_id"])
                event_copy["organizer"] = self.get_organizer_by_id(event["organizer_id"])
                event_copy["type"] = self.get_type_by_id(event["type_id"])
                
                events_with_details.append(event_copy)
            
            return tuple(events_with_details)

    def get_events(self):
        self.cur.execute("SELECT * FROM tevents ORDER BY id")
        self.events = self.cur.fetchall()
        self.events = self.get_details(self.events)
        close_cursor(self.cur)
        return self.events
    
    def get_event_with_id(self, id_event):
        self.cur.execute("SELECT * FROM tevents WHERE id = %s", (id_event,))
        event = self.cur.fetchone()
        event = self.get_details(event)
        close_cursor(self.cur)
        return event
    
    def get_filtered_events(self, start_date=None, end_date=None, type_id=None, budget=None):
        query = "SELECT * FROM tevents WHERE 1=1"
        params = []
        
        if start_date is not None:
            query += " AND date >= %s"
            params.append(start_date)
        
        if end_date is not None:
            query += " AND date <= %s"
            params.append(end_date)
        
        if type_id is not None:
            if len(type_id) > 1:
                values = ', '.join(['%s'] * len(type_id))
                query += f" AND type_id IN ({values})"
                params.extend(type_id)
            else:
                query += " AND type_id = %s"
                params.append(type_id)
        
            if budget is not None:
                query += " AND budget <= %s"
                params.append(budget)
        
        # Ejecutar la consulta con los parámetros
        self.cur.execute(query, tuple(params))
        self.events = self.cur.fetchall()
        self.events = self.get_details(self.events)
        close_cursor(self.cur)
        return self.events

    def get_events_by_date_range(self, start_date, end_date):
        return self.get_filtered_events(start_date=start_date, end_date=end_date)

    def get_events_by_type(self, type_id):
        return self.get_filtered_events(type_id=type_id)

    def get_events_by_budget(self, max_budget):
        return self.get_filtered_events(budget=max_budget)
    
    def get_featured_events(self):
        query = f"SELECT * FROM tevents WHERE date >= '{date.today()}' AND date <= '{date.today() + timedelta(7)}'"
        self.cur.execute(query)
        self.events = self.cur.fetchall()
        self.events = self.get_details(self.events)
        close_cursor(self.cur)
        return self.events