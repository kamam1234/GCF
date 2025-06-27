from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "59dad7ea5ef71a3070a5e5d33b1d2868"

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    if request.method == "POST":
        city = request.form["city"].strip()
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        print("Request URL:", url)  # DEBUG: See the exact URL
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"],
                "icon": data["weather"][0]["icon"]
            }
        else:
            print("Error:", response.status_code, response.text)  # Debugging
            weather_data = {"error": "City not found or API error!"}
    return render_template("index.html", weather=weather_data)

if __name__ == "__main__":
    app.run(debug=True)
