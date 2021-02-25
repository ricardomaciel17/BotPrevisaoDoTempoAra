from datetime import datetime, timedelta
import time
import sleeper
import bot_main 

while True:
    ActualTime = datetime.utcnow()
    SaoPauloTime = ActualTime - timedelta(hours = 3) 
    SaoPauloTime = SaoPauloTime.strftime("%H:%M:%S")
    if SaoPauloTime > '21:45:00' and SaoPauloTime < '22:15:00':
        bot_main.funcao_bot()
    else:
        sleeper.sleeping()