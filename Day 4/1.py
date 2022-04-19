# A Python program to find the details of a given zip code using the Nominatim API and GeoPy package.
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="geoapi")

place = input ("Enter zip code:")

location = geolocator.geocode(place)
print(location.address)