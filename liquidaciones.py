from db import get_connection, crear_tabla_liquidaciones_oca

def guardar_liquidacion(
    tanque,
    api,
    temperatura,
    volumen_recibido,
    volumen_calculado,
    tolerancia,
    diferencia,
    resultado,
    fecha
):
    # -------------------------
    # VALIDACIÓN ANTI-None
    # -------------------------
    if None in (
        tanque,
        api,
        temperatura,
        volumen_recibido,
        volumen_calculado,
        tolerancia,
        diferencia,
        resultado,
        fecha
    ):
        raise ValueError("❌ Hay campos None en guardar_liquidacion_oca")

    conn = get_connection()
    cursor = conn.cursor()

    sql = """
        INSERT INTO liquidaciones_oca (
            tanque,
            api,
            temperatura,
            volumen_recibido,
            volumen_calculado,
            tolerancia,
            diferencia,
            resultado,
            fecha
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    cursor.execute(sql, (
        str(tanque),
        float(api),
        float(temperatura),
        float(volumen_recibido),
        float(volumen_calculado),
        float(tolerancia),
        float(diferencia),
        resultado,
        fecha
    ))

    conn.commit()
    cursor.close()
    conn.close()
