from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "8b904582bc03e881a53657ef8342fab5"  # <-- Add your OpenWeatherMap API Key here
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.route("/", methods=["GET", "POST"])
def home():
    weather_data = None

    if request.method == "POST":
        city = request.form["city"]
        
        # Build API URL
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data["cod"] == 200:
            weather_data = {
                "city": city,
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "description": data["weather"][0]["description"].title(),
                "icon": data["weather"][0]["icon"]
            }
        else:
            weather_data = "City not found"

    return render_template("index.html", weather=weather_data)

if __name__ == "__main__":
    app.run(debug=True)
