import os
import mysql.connector

# 🔹 SOLO carga .env si estás en LOCAL
if os.getenv("RAILWAY_ENVIRONMENT") is None:
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except:
        pass

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("MYSQLHOST"),
        port=int(os.getenv("MYSQLPORT", 3306)),
        user=os.getenv("MYSQLUSER"),
        password=os.getenv("MYSQLPASSWORD"),
        database=os.getenv("MYSQLDATABASE"),
        autocommit=True
    )

def crear_tabla_liquidaciones_oca():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS liquidaciones_oca (
            id INT AUTO_INCREMENT PRIMARY KEY,
            tanque VARCHAR(50),
            api FLOAT,
            temperatura FLOAT,
            volumen_recibido FLOAT,
            volumen_calculado FLOAT,
            tolerancia FLOAT,
            diferencia FLOAT,
            resultado VARCHAR(50),
            fecha DATETIME
        )
    """)

    cursor.close()
    conn.close()
