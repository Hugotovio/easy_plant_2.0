from db import get_connection

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS liquidaciones (
        id INT AUTO_INCREMENT PRIMARY KEY,
        tanque INT NOT NULL,
        api FLOAT,
        temperatura FLOAT,
        volumen_recibido FLOAT,
        volumen_calculado FLOAT,
        tolerancia FLOAT,
        diferencia FLOAT,
        resultado VARCHAR(20),
        fecha DATETIME
    )
    """)

    cursor.close()
    conn.close()
    print("✅ Tabla liquidaciones verificada / creada")
