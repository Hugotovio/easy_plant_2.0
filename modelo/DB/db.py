import os
import mysql.connector
import dotenv

dotenv.load_dotenv()

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("MYSQLHOST"),
        port=int(os.getenv("MYSQLPORT")),
        user=os.getenv("MYSQLUSER"),
        password=os.getenv("MYSQLPASSWORD"),
        database=os.getenv("MYSQLDATABASE"),
        autocommit=True
    )


def crear_tabla_liquidaciones_ctg():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS liquidaciones (
            id INT AUTO_INCREMENT PRIMARY KEY,
            tanque VARCHAR(50) NOT NULL,
            altura_inicial INT NOT NULL,
            altura_final INT NOT NULL,
            volumen_bruto DECIMAL(10,2) NOT NULL,
            volumen_neto DECIMAL(10,2) NOT NULL,
            api_observado DECIMAL(5,2) NOT NULL,
            api_corregido DECIMAL(5,2) NOT NULL,
            temperatura DECIMAL(5,2) NOT NULL,
            fecha DATE NOT NULL,
            hora TIME NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cursor.close()
    conn.close()
