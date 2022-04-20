# A Python program to calculate the distance between Cairo and Nairobi City.
import haversine as hs
def distance_between():
    Nairobi = (0.0236,37.9062)
    Cairo =  (30.0444,31.2357)
    # Output the distance in Kilometers
    hs.haversine(Nairobi, Cairo,)
    from geopy.distance import geodesic
    Cairo = (30.0444, 31.2357)
    Nairobi = (1.2921, 36.8219)
    print(geodesic(Cairo,Nairobi).kilometers,"kilometers")

distance_between()