# IP2KML
IP Address to Google Earth KML file

## How this script works?

- Takes user input of an IP Address.
- Sends the IP Address user input to ip-api.com as a JSON string.
- ip-api.com gets the JSON string of the IP Address and finds the Longitude and Latitude of the IP Address.
- Then the script creates a KML file, which you can use on Google Earth, to view the location of the IP Address plotted on a map.


## Requirements

```python
pip3 install requests, simplekml
```

## Usage

Ensure you give the script permissions to execute. Do the following from the terminal:
```bash
sudo chmod +x ip2kml.py
```

Now you can run the script as follows in the terminal:

```python
python3 ip2kml.py
```

## Example script

```python
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

```

## License Information

This library is released under the [Creative Commons ShareAlike 4.0 International license](https://creativecommons.org/licenses/by-sa/4.0/). You are welcome to use this library for commercial purposes. For attribution, we ask that when you begin to sell your device using our footprint, you email us with a link to the product being sold. We want bragging rights that we helped (in a very small part) to create your 8th world wonder. We would like the opportunity to feature your device on our homepage.
