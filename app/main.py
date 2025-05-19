# app/main.py

import time
from tesla_api import get_vehicle_location
from eta_calculator import get_eta
from notifications import send_sms_alert

# SET THIS to your fixed destination coordinates (e.g., home, office)
DEST_LAT = 40.289807561258684  # Replace with your real latitude
DEST_LON =  -74.71416691982994  # Replace with your real longitude

def check_and_alert():
    # 1. Get car location
    car_lat, car_lon = get_vehicle_location()
    print(f"Car is at {car_lat}, {car_lon}")

    # 2. Calculate ETA
    eta = get_eta((car_lat, car_lon), (DEST_LAT, DEST_LON))
    print(f"ETA from car to destination: {eta:.1f} minutes")

    # 3. If ETA <= 5 min, send SMS
    if eta <= 5:
        send_sms_alert(f"🚗 Your Tesla is less than 5 minutes away from your destination!")
        print("Alert sent!")
    else:
        print("Car is not within 5 minutes yet. No alert sent.")
    

if __name__ == "__main__":
    # You can loop this to check every X minutes if you want
    check_and_alert()