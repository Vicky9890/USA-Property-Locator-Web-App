from flask import Flask, render_template, request
import requests
import folium

app = Flask(__name__)

def geocode_address(address):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": address,
        "format": "json",
        "limit": 1
    }
    headers = {"User-Agent": "property-locator"}
    response = requests.get(url, params=params, headers=headers).json()
    if not response:
        return None
    return float(response[0]["lat"]), float(response[0]["lon"])

def get_boundary(lat, lon, delta=0.00045):
    return {
        "South Latitude": round(lat - delta, 6),
        "North Latitude": round(lat + delta, 6),
        "West Longitude": round(lon - delta, 6),
        "East Longitude": round(lon + delta, 6)
    }

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    map = None
    error = None

    if request.method == "POST":
        address = request.form["address"]
        geo = geocode_address(address)
        
        if not geo:
            error = "Address not found or Invalid. Please enter a valid USA address."

        else:
            lat, lon = geo
            boundary = get_boundary(lat, lon)
            m = folium.Map(location=[lat, lon], zoom_start=17)
            folium.Marker(
                [lat, lon],
                popup=address,
                tooltip="Property Location"
            ).add_to(m)

            map = m._repr_html_()
            result = {
                "address": address,
                "boundary": boundary,
                "latitude": lat,
                "longitude": lon
            }

    return render_template("index.html", result=result, map=map, error=error)

if __name__ == "__main__":
    app.run(debug=True)


