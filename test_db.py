from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv()

print("MYSQLHOST:", os.getenv("MYSQLHOST"))
print("MYSQLPORT:", os.getenv("MYSQLPORT"))
print("MYSQLUSER:", os.getenv("MYSQLUSER"))
print("MYSQLDATABASE:", os.getenv("MYSQLDATABASE"))

try:
    conn = mysql.connector.connect(
        host=os.getenv("MYSQLHOST"),
        port=int(os.getenv("MYSQLPORT")),
        user=os.getenv("MYSQLUSER"),
        password=os.getenv("MYSQLPASSWORD"),
        database=os.getenv("MYSQLDATABASE"),
        connection_timeout=5
    )
    print("✅ Conexión exitosa a MySQL Railway")
    conn.close()
except Exception as e:
    print("❌ Error de conexión:", e)
