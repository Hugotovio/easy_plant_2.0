from db import get_connection

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS liquidaciones (
        id INT AUTO_INCREMENT PRIMARY KEY,
        tanque INT NOT NULL,
        api DECIMAL(5,2) NOT NULL,
        temperatura DECIMAL(5,2) NOT NULL,
        volumen_recibido DECIMAL(10,2) NOT NULL,
        volumen_calculado DECIMAL(10,2) NOT NULL,
        tolerancia DECIMAL(10,2) NOT NULL,
        diferencia DECIMAL(10,2) NOT NULL,
        resultado VARCHAR(20) NOT NULL,
        fecha DATETIME NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    cursor.close()
    conn.close()
