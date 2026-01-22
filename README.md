# USA Property Locator Web App
A simple Flask-based web application that allows users to input a **USA address** and retrieve its **latitude, longitude, boundary dimensions** and **property location on a live map** using real-time geocoding data. The app focuses on core functionality, real-time validation and graceful handling of invalid addresses

## Features

-  Accepts any valid **USA address**
-  Fetches **latitude & longitude** using OpenStreetMap (Nominatim API)
-  Calculates **boundary dimensions** (North, South, East, West)
-  Displays property location on an **interactive map**
-  Handles **invalid or incorrect addresses** gracefully
-  Uses **live data**, ideal for real-time demos

## Technology Used

- **Backend:** Python, Flask  
- **Geocoding:** OpenStreetMap (Nominatim)  
- **Mapping:** Folium  
- **Frontend:** HTML, CSS  
- **HTTP Requests:** Requests 

## Requirements

To run this project, ensure the following Python packages are installed:

- flask
- requests
- folium

All required dependencies are listed in the ```requirements.txt``` file.

## Boundary Dimensions Calculation Logic

The boundary dimensions are calculated using a small delta value:

```python
def get_boundary(lat, lon, delta=0.00045):
```

- `delta` represents a small geographic offset (~50 meters)
- Used to approximate property boundaries

## Error Handling

- Displays an error message for invalid or unknown addresses
- Prevents incorrect map rendering

## Output
<img width="1849" height="925" alt="image" src="https://github.com/user-attachments/assets/83a57a42-281b-4c53-987b-d0436038639b" />
<img width="1880" height="929" alt="image" src="https://github.com/user-attachments/assets/6a46f8d3-ba52-4e61-9351-bcfe251f6c28" />


