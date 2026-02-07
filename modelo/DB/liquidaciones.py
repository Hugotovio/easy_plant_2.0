from modelo.DB.db import get_connection,crear_tabla_liquidaciones_ctg

def guardar_liquidacion(
    tanque,
    altura_inicial,
    altura_final,
    volumen_bruto,
    volumen_neto,
    api_observado,
    api_corregido,
    temperatura,
    fecha,
    hora
):  
    crear_tabla_liquidaciones_ctg()
    print("Guardando liquidación en la base de datos...")
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
        INSERT INTO liquidaciones (
            tanque,
            altura_inicial,
            altura_final,
            volumen_bruto,
            volumen_neto,
            api_observado,
            api_corregido,
            temperatura,
            fecha,
            hora
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    valores = (
        tanque,
        altura_inicial,
        altura_final,
        volumen_bruto,
        volumen_neto,
        api_observado,
        api_corregido,
        temperatura,
        fecha,
        hora
    )

    cursor.execute(sql, valores)
    cursor.close()
    conn.close()
