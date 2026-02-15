import pytz
from datetime import datetime

zona_horaria = pytz.timezone('America/Bogota')
tiempo_actual = datetime.now(zona_horaria)

def hora():
    hora_str = tiempo_actual.strftime('%H:%M:%S')  # solo hora:minutos:segundos
    print(hora_str)

hora()