# IP2KML
IP Address to Google Earth KML file

## How this script works?

- Takes user input of an IP Address.
- Sends the IP Address user input to ip-api.com as a JSON string.
- ip-api.com gets the JSON string of the IP Address and finds the Longitude and Latitude of the IP Address.
- Then the script creates a KML file, which you can use on Google Earth, to view the location of the IP Address plotted on a map.


## Requirements

> pip3 install requests, simplekml


## License Information

This library is released under the [Creative Commons ShareAlike 4.0 International license](https://creativecommons.org/licenses/by-sa/4.0/). You are welcome to use this library for commercial purposes. For attribution, we ask that when you begin to sell your device using our footprint, you email us with a link to the product being sold. We want bragging rights that we helped (in a very small part) to create your 8th world wonder. We would like the opportunity to feature your device on our homepage.
