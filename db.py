import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
load_dotenv()


def get_connection():
    return mysql.connector.connect(
        host=os.getenv("MYSQLHOST"),
        port=int(os.getenv("MYSQLPORT")),
        user=os.getenv("MYSQLUSER"),
        password=os.getenv("MYSQLPASSWORD"),
        database=os.getenv("MYSQLDATABASE"),
        autocommit=True
    )


def crear_tabla_liquidaciones_oca():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
        CREATE TABLE IF NOT EXISTS liquidaciones_oca (
            id INT AUTO_INCREMENT PRIMARY KEY,
            tanque VARCHAR(20),
            api DECIMAL(6,2),
            temperatura DECIMAL(6,2),
            volumen_recibido DECIMAL(12,2),
            volumen_calculado DECIMAL(12,2),
            tolerancia DECIMAL(12,2),
            diferencia DECIMAL(12,2),
            resultado VARCHAR(20),
            fecha DATETIME,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """

        cursor.execute(sql)
        cursor.close()
        conn.close()

        print("✅ Tabla liquidaciones_oca verificada / creada correctamente")

    except Error as e:
        print("❌ Error creando tabla liquidaciones_oca:", e)
