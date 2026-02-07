
from modelo.DB.liquidaciones import guardar_liquidacion

class liquidacion:
    def __init__(self,tanque, altura_inicial, altura_final, volumen_bruto, volumen_neto, 
                 api_observado, api_corregido, temperatura,fecha, hora):
        self.tanque = tanque
        self.altura_inicial = altura_inicial
        self.altura_final = altura_final
        self.volumen_bruto = volumen_bruto
        self.volumen_neto = volumen_neto
        self.api_observado = api_observado
        self.api_corregido = api_corregido
        self.temperatura = temperatura
        self.fecha = fecha
        self.hora = hora
    def guardar(self):
        guardar_liquidacion(
            self.tanque,
            self.altura_inicial,
            self.altura_final,
            self.volumen_bruto,
            self.volumen_neto,
            self.api_observado,
            self.api_corregido,
            self.temperatura,
            self.fecha,
            self.hora
        )
    