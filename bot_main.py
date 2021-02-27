# -*- coding: utf-8 -*-
#Developed By Ricardo Maciel
#version 1.1

import tweepy, urllib.request, json, datetime, sleeper
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
    today = datetime.date.today()
    NextDay = today + datetime.timedelta(days = 1) 
    NextDay = NextDay.strftime("%d/%m")
    for values in data['forecast']:
        days = values['date']
        if days == NextDay:
            break
    Day = values['date']
    MaxTemp = values['max']
    MinTemp = values['min']
    Description = values['description']

    if Description == ('Ensolarado com muitas nuvens'):
        Description = ('Clima ensolarado com muitas nuvens')
    Tweet = ('A previsão do tempo para amanhã em Araranguá, '+str(Day)+', é de um dia com '+Description+
            ', com minima de '+str(MinTemp)+'° e maxima de '+str(MaxTemp)+'°')
    try:
        api.update_status(Tweet)
        sleeper.sleeping()
        import timer
    except tweepy.TweepError as Error:
        api.update_status(Error)
        exit()

