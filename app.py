import requests 
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods =["GET", "POST"])
def index():
    weatherData = ''
    error = 0
    cityName = ''
    if request.method == "POST":
        cityName = request.form.get("cityName")
        if cityName:
            weatherApiKey = 'f57726ca0fec25e022b1cc6c6fae8697'
            url_city = "http://api.openweathermap.org/geo/1.0/direct?q=" + cityName + "&appid=" + weatherApiKey
            coordinates = requests.get(url_city).json() 
            url = "https://api.openweathermap.org/data/2.5/weather?lat=" + str(coordinates[0]["lat"]) + "&lon=" + str(coordinates[0]["lon"]) + "&appid=" + weatherApiKey
            weatherData = requests.get(url).json()
        else:
            error = 1
    return render_template('index.html', data = weatherData, cityName = cityName, error = error)

if __name__ == "__main__":
    app.run()

    