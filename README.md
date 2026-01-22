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
<img width="1869" height="916" alt="image" src="https://github.com/user-attachments/assets/c918223e-6ee7-4cac-826a-9d799bd7dc9b" />
<img width="1864" height="926" alt="image" src="https://github.com/user-attachments/assets/6845f72a-42e9-48c2-ae75-74f0194693e2" />



