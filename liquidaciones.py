from db import get_connection

def guardar_liquidacion(
    tanque,
    altura_inicial,
    altura_final,
    volumen_bruto,
    volumen_neto,
    api_observado,
    api_corregido,
    temperatura,
    resultado,
    fecha,
    hora
):
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
            resultado,
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
        resultado,
        fecha,
        hora
    )

    cursor.execute(sql, valores)
    cursor.close()
    conn.close()
