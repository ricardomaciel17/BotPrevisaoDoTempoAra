# -*- coding: utf-8 -*-
#Developed By Ricardo Maciel
#version 1.2.1

import tweepy, urllib.request, json, datetime, sleeper, spClock
from dotenv import load_dotenv
load_dotenv('key.env')
def funcao_bot():
    import os
    consumer_key = os.getenv("consumer_key")
    consumer_secret = os.getenv("consumer_secret")
    access_token = os.getenv("access_token")
    access_token_secret = os.getenv("access_token_secret")
    forecast_io_apikey =  os.getenv("forecast_io_apikey")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    url = "https://api.hgbrasil.com/weather?woeid=456048&array_limit=2&fields=only_results,temp,city_name,forecast,max,min,date,description&key="+str(forecast_io_apikey)
    response = urllib.request.urlopen(url);
    data = json.loads(response.read())
    today = spClock.funcao_horario_sp()
    nextDay = today + datetime.timedelta(days = 1)
    dayTweet = nextDay.strftime("%d/%m/%y")
    nextDay = nextDay.strftime("%d/%m")

    for values in data['forecast']:
        days = values['date']
        if days == nextDay:
            break

    maxTemp = values['max']
    minTemp = values['min']
    description = values['description']

    if description == ('Ensolarado com muitas nuvens') or description == ('Parcialmente nublado'):
        description = ('tempo '+description)
    tweet = ('A previsão do tempo para amanhã em Araranguá, '+str(dayTweet)+', é de um dia com '+description+
            ', com minima de '+str(minTemp)+'° e maxima de '+str(maxTemp)+'°')
    try:
        api.update_status(tweet)
        sleeper.sleeping()
        import timer
    except tweepy.TweepError as Error:
        api.update_status(Error)
        exit()