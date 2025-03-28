from datetime import timedelta, date
from app.utils.db_utils import get_cursor, close_cursor
# Clase que se encarga de manejar los eventos con instrucciones SQL para llamar a la base de datos
class EventModel:
    # Constructor de la clase
    def __init__(self):
        self.events = ()
        self.cur = get_cursor()
        self.location = ()
        self.organizer = ()
        self.type = ()
# Funcion para obtener la ubicacion de un evento por su id
    def get_location_by_id(self, id_location):
        self.cur.execute("SELECT * FROM tlocations WHERE id = %s", (id_location,))
        self.location = self.cur.fetchone()
        return self.location
# Funcion para obtener el organizador de un evento con el id
    def get_organizer_by_id(self, id_organizer):
        self.cur.execute("SELECT * FROM torganizers WHERE id = %s", (id_organizer,))
        self.organizer = self.cur.fetchone()
        return self.organizer
# Funcion para obtener el tipo de un evento con el id
    def get_type_by_id(self, id_type):
        self.cur.execute("SELECT * FROM tevent_types WHERE id = %s", (id_type,))
        self.type = self.cur.fetchone()
        return self.type
# Funcion para obtener los detalles de un evento
    def get_details(self, events_data):
        if isinstance(events_data, dict):
            events_data["location"] = self.get_location_by_id(events_data["location_id"])
            events_data["organizer"] = self.get_organizer_by_id(events_data["organizer_id"])
            events_data["type"] = self.get_type_by_id(events_data["type_id"])

            #convertir campos timedelta a segundos
            for key, value in events_data.items():
                if isinstance(value, timedelta):
                    events_data[key] = value.total_seconds()  # O str(value)
            return events_data
        else:
            events_with_details = []
            for event in events_data:
                event_copy = dict(event)

                event_copy["location"] = self.get_location_by_id(event["location_id"])
                event_copy["organizer"] = self.get_organizer_by_id(event["organizer_id"])
                event_copy["type"] = self.get_type_by_id(event["type_id"])

                #convertir campos timedelta a segundos
                for key, value in event_copy.items():
                    if isinstance(value, timedelta):
                        event_copy[key] = value.total_seconds()  # O str(value)

                events_with_details.append(event_copy)
            #regresamos los eventos en un tuple
            return tuple(events_with_details)
# Func para obtener todos los eventos
    def get_events(self):
        self.cur.execute("SELECT * FROM tevents ORDER BY id")
        self.events = self.cur.fetchall()
        self.events = self.get_details(self.events)
        close_cursor(self.cur)
        return self.events
# Func para obtener un evento por su id
    def get_event_with_id(self, id_event):
        self.cur.execute("SELECT * FROM tevents WHERE id = %s", (id_event,))
        event = self.cur.fetchone()
        event = self.get_details(event)
        close_cursor(self.cur)
        return event
# Func para eventos filtrados 
    def get_filtered_events(self, start_date=None, end_date=None, id=None, budget=None):
        query = "SELECT * FROM tevents WHERE 1=1"
        params = []
    
        # Filtro de fechas
        if start_date is not None:
            query += " AND date >= %s"
            params.append(start_date)
        if end_date is not None:
            query += " AND date <= %s"
            params.append(end_date)
        
        # Filtro de categorías (usando id en lugar de type_id)
        if id is not None:
            # Si es una lista
            if isinstance(id, list):
                # Convertir a lista de enteros si no lo están
                id = [int(t) for t in id]
                
                # Si la lista no está vacía
                if id:
                    placeholders = ', '.join(['%s'] * len(id))
                    query += f" AND id IN ({placeholders})"
                    params.extend(id)
            else:
                # Si es un solo valor
                query += " AND id = %s"
                params.append(int(id))
        
        # Filtro de presupuesto
        if budget is not None:
            query += " AND budget <= %s"
            params.append(budget)
        
        query += " ORDER BY date"
        
        print("Consulta final:", query)  # Debug
        print("Parámetros:", params)     # Debug
        
        try:
            self.cur = get_cursor()  # Restablecer el cursor
            self.cur.execute(query, tuple(params))
            self.events = self.cur.fetchall()
            self.events = self.get_details(self.events)
            print(self.events)
            return self.events
        except Exception as e:
            print("Error en la consulta:", str(e))  # Debug
            raise
        finally:
            close_cursor(self.cur)