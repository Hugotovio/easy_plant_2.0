import os
import mysql.connector

def get_connection(database=None):
    return mysql.connector.connect(
        host=os.getenv("MYSQLHOST"),
        port=int(os.getenv("MYSQLPORT")),
        user=os.getenv("MYSQLUSER"),
        password=os.getenv("MYSQLPASSWORD"),
        database=database or os.getenv("MYSQLDATABASE"),
        autocommit=True
    )
