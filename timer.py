from datetime import datetime, timedelta
import sleeper
import bot_main

while True:
    ActualTime = datetime.utcnow()
    SaoPauloTime = ActualTime - timedelta(hours=3)
    SaoPauloTime = SaoPauloTime.strftime("%H:%M:%S")
    if SaoPauloTime > '22:00:00' and SaoPauloTime < '22:30:00':
        bot_main.funcao_bot()
    else:
        sleeper.sleeping()

