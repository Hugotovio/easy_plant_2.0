import os
import mysql.connector

# SOLO usar dotenv en local
if os.getenv("RAILWAY_ENVIRONMENT") is None:
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except:
        pass

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("MYSQLHOST"),
        port=int(os.getenv("MYSQLPORT")),
        user=os.getenv("MYSQLUSER"),
        password=os.getenv("MYSQLPASSWORD"),
        database=os.getenv("MYSQLDATABASE"),
        autocommit=True
    )
