import os

basedir = os.path.abspath(os.path.dirname(__file__)) 

WEATHER_DEFAULT_CITY = "Moscow,Russia"
WEATHER_API_KEY = "2dfbfdc296a1419e811122228191803"
WEATHER_URL = "http://api.worldweatheronline.com/premium/v1/weather.ashx"
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db')