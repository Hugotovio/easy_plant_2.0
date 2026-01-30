from db import get_connection

def guardar_liquidacion(data):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    INSERT INTO liquidaciones
    (tanque, api, temperatura, volumen_recibido,
     volumen_calculado, tolerancia, diferencia, resultado, fecha)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    valores = (
        data["tanque"],
        data["api"],
        data["temperatura"],
        data["volumen_recibido"],
        data["volumen_calculado"],
        data["tolerancia"],
        data["diferencia"],
        data["resultado"],
        data["fecha"]
    )

    cursor.execute(sql, valores)
    conn.commit()
    cursor.close()
    conn.close()


# =========================
# INVENTARIO ACTUAL POR TANQUE ✅
# =========================
def obtener_inventario_actual():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    sql = """
    SELECT 
        l.tanque,
        l.api,
        l.temperatura
    FROM liquidaciones l
    WHERE l.fecha = (
        SELECT MAX(l2.fecha)
        FROM liquidaciones l2
        WHERE l2.tanque = l.tanque
    )
    ORDER BY CAST(l.tanque AS UNSIGNED)
    """

    cursor.execute(sql)
    data = cursor.fetchall()

    cursor.close()
    conn.close()
    return data