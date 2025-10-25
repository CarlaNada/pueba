from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Diccionario de ciudades con latitudes y longitudes
ciudades = {
    "Buenos Aires": {"lat": -34.6037, "lon": -58.3816},
    "Córdoba": {"lat": -31.4201, "lon": -64.1888},
    "Madrid": {"lat": 40.4168, "lon": -3.7038},
    "Nueva York": {"lat": 40.7128, "lon": -74.0060},
    "Tokio": {"lat": 35.6895, "lon": 139.6917},
    "París": {"lat": 48.8566, "lon": 2.3522},
    "Londres": {"lat": 51.5074, "lon": -0.1278},
    "Sídney": {"lat": -33.8688, "lon": 151.2093},
    "Ciudad de México": {"lat": 19.4326, "lon": -99.1332},
    "El Cairo": {"lat": 30.0444, "lon": 31.2357}
}

@app.route("/")
def index():
    return render_template("index.html", ciudades=ciudades)

@app.route("/clima")
def clima():
    nombre_ciudad = request.args.get("ciudad")

    if not nombre_ciudad or nombre_ciudad not in ciudades:
        return "Ciudad no válida", 400

    lat = ciudades[nombre_ciudad]["lat"]
    lon = ciudades[nombre_ciudad]["lon"]

    # URL de la API
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

    try:
        respuesta = requests.get(url)
        datos = respuesta.json()
        clima_actual = datos["current_weather"]
    except Exception as e:
        return f"Error al obtener datos del clima: {e}"

    return render_template("clima.html", ciudad=nombre_ciudad, clima=clima_actual)

if __name__ == "__main__":
    app.run(debug=True)
