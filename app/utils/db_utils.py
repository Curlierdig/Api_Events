from app.database.db import mysql

def get_cursor():
    """ 
    Return a cursor to execute queries to the database.
    """
    return mysql.connection.cursor()

def commit_changes():
    """
    Confirm the changes made to the database.
    """
    mysql.connection.commit()

def close_cursor(cursor):
    """
    Close the cursor when it's no longer needed.
    """
    if cursor:
        cursor.close()