import sleeper
import bot_main
import spClock

while True:
    saoPauloTime = spClock.funcao_horario_sp()
    saoPauloTime = saoPauloTime.strftime("%H:%M:%S")
    if '22:30:00' < saoPauloTime < '22:45:00':
        bot_main.funcao_bot()
    else:
        sleeper.sleeping()