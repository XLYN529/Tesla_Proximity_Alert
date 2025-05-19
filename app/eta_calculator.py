# app/eta_calculator.py

import os
from dotenv import load_dotenv
import requests

# Load environment variables
load_dotenv()
ORS_API_KEY = os.getenv("ORS_API_KEY")

def get_eta(car_coords, dest_coords):
    """
    Calculate ETA (in minutes) from car to destination using OpenRouteService.
    car_coords and dest_coords are (lat, lon) tuples.
    """
    url = 'https://api.openrouteservice.org/v2/directions/driving-car'
    headers = {
        'Authorization': ORS_API_KEY,
        'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8'
    }
    params = {
        'start': f"{car_coords[1]},{car_coords[0]}",
        'end': f"{dest_coords[1]},{dest_coords[0]}"
    }
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    # Extract duration in seconds and convert to minutes
    eta_seconds = data['features'][0]['properties']['segments'][0]['duration']
    eta_minutes = eta_seconds / 60
    return eta_minutes

# Test example:
if __name__ == "__main__":
    # Example coordinates (replace with real values for your use!)
    car = (40.7128, -74.0060)       # e.g., Tesla's current location (lat, lon)
    dest = (40.5000, -74.4500)      # e.g., Your home location (lat, lon)
    eta = get_eta(car, dest)
    print(f"ETA from car to destination: {eta:.1f} minutes")