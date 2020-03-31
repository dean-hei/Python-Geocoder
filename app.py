import geocoder
import requests

api_key=open('apikey.txt', 'r').read()
API_BASE_URL = "https://api.darksky.net/forecast/" + api_key

# Declare destinations list here.
destinations = ["The Space Needle",
  "Crater Lake",
  "The Golden Gate Bridge",
  "Yosemite National Park",
  "Las Vegas, Nevada",
  "Grand Canyon National Park",
  "Aspen, Colorado",
  "Mount Rushmore",
  "Yellowstone National Park",
  "Sandpoint, Idaho",
  "Banff National Park",
  "Capilano Suspension Bridge"]

# Loop through each destination.
for point in destinations:
    #   Get the lat-long coordinates from `geocoder.arcgis`.
    loc = geocoder.arcgis(point)
    #   Print out the place name and the coordinates.
    print("{0} is located at ({1:.4f}, {2:.4f})".format(point, loc.latlng[0], loc.latlng[1]))

    full_api_url = API_BASE_URL + "/{1:.4f},{2:.4f}".format(point, loc.latlng[0], loc.latlng[1])
    result = requests.request('GET', full_api_url).json()

    # From the result, print out the summary and current temperature.
    print("At {0} right now, it's {1} with a temperature of {2}° F\n".format(point, result["currently"]["summary"], result["currently"]["temperature"]))    
