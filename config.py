class Config:
    # Configuración de MySQL
    DB_HOST = 'localhost'
    DB_USER = 'root'
    DB_PASSWORD = ''
    DB_NAME = 'events_db'
    DB_PORT = 3306
    DB_CURSORCLASS = 'DictCursor'  # Para obtener resultados en formato diccionario