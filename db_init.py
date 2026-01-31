from db import get_connection

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS inventario")
    cursor.close()
    conn.close()

    conn = get_connection("inventario")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS liquidaciones (
            id INT AUTO_INCREMENT PRIMARY KEY,
            tanque VARCHAR(20) NOT NULL,
            galones DECIMAL(10,2) NOT NULL,
            api DECIMAL(5,2) NOT NULL,
            temperatura DECIMAL(5,2) NOT NULL,
            fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cursor.close()
    conn.close()
