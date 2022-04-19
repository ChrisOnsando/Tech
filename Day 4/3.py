# A Python function to get the city, state and country name of a specified latitude and longitude using Nominatim API and Geopy package.
from geopy import location
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="locationfinder")
# This are the specified latitude and longitude to get the city of Alberta,Canada
# Latitude = "53.01669802"
# Longitude = "-112.8166386"
def get_city(coordinates):
# Location = geolocator.reverse(Latitude+ ","+Longitude)
    Location = geolocator.reverse(coordinates,exactly_one=True)
    address = Location.raw['address']
    city_name = address.get('city')
    state_name = address.get('state')
    country_name = address.get('country')
    return city_name, state_name, country_name
print(get_city("53.01669802,-112.8166386"))