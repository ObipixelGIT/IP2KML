# -*- coding: utf-8 -*-
# Author : Dimitrios Zacharopoulos
# All copyrights to Obipixel Ltd
# 28 March 2023

import requests
from simplekml import Kml, Style, Color

def get_location(ip_address):
    response = requests.get(f"http://ip-api.com/json/{ip_address}")
    if response.status_code != 200:
        raise Exception(f"Failed to get location for IP address {ip_address}")
    data = response.json()
    if data["status"] == "fail":
        raise Exception(f"Failed to get location for IP address {ip_address}: {data['message']}")
    return data["lon"], data["lat"]

if __name__ == "__main__":
    ip_address = input("Enter the IP address you want to look up: ")
    try:
        longitude, latitude = get_location(ip_address)
        kml = Kml()
        point = kml.newpoint(name=ip_address, coords=[(longitude, latitude)])
        point.style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/pal3/icon21.png'
        point.style.labelstyle.color = Color.red  # Make the label red
        kml.save(f"{ip_address}.kml")
        print(f"KML file saved as {ip_address}.kml")
    except Exception as e:
        print(e)
