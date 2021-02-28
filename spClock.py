import pytz
from datetime import datetime

def funcao_horario_sp():
    spTimeZone = pytz.timezone('America/Sao_Paulo')
    saoPauloTime = datetime.now(tz=spTimeZone)
    return saoPauloTime