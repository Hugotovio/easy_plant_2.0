import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",   # XAMPP por defecto no tiene contraseña
        database="easy_plant"
    )
