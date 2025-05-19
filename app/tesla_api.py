# app/tesla_api.py

import os
from dotenv import load_dotenv
import teslapy

load_dotenv()

TESLA_EMAIL = os.getenv("TESLA_EMAIL")

def get_vehicle_location():
    with teslapy.Tesla(TESLA_EMAIL) as tesla:
        if not tesla.authorized:
            print("Go to the URL below and log in to Tesla:")
            print(tesla.authorization_url())
            tesla.fetch_token(authorization_response=input("Enter full callback URL: "))
        vehicles = tesla.vehicle_list()
        if not vehicles:
            raise Exception("No Tesla vehicles found for this account.")
        car = vehicles[0]
        car.sync_wake_up()  # <--- This wakes up the car if it's asleep!
        drive_state = car['drive_state']
        latitude = drive_state['latitude']
        longitude = drive_state['longitude']
        return latitude, longitude

if __name__ == "__main__":
    lat, lon = get_vehicle_location()
    print(f"Current Tesla location: {lat}, {lon}")