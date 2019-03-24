from flask import Flask
from weather import weather_by_city

app = Flask(__name__)

@app.route('/')  #когда клиент заходит на главную страницу
def index():
    weather = weather_by_city('Moscow, Russia')
    if weather:
        return f"Температура: {weather['temp_C']}°C, ощущается как {weather['FeelsLikeC']}°C"
    else:
        return 'Сервис временно недоступен'

if __name__ == "__main__":   #если файл запускается напрямую - запускаем приложение
    app.run()
