# A Python program to search the country name from a given state name using the Nominatim API and GeoPy package
from geopy.geocoders import Nominatim
def country_name():

    geolocator = Nominatim(user_agent="country")

    state = "Newfoundland And Labrador"

    location = geolocator.geocode(state)

    print('The Country is: ' , location.address)

country_name()