# https://www.youtube.com/watch?v=Geisa_ib5hs

import phonenumbers

import folium

from my_number import number

from phonenumbers import geocoder

Key = '42d1c121fe8b49609aaa246534dac44e'

samNumber = phonenumbers.parse(number)
yourLocation = geocoder.description_for_number(samNumber, "en")
print(yourLocation)

# get service.provider

from phonenumbers import carrier
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(Key)

query = str(yourLocation)
results = geocoder.geocode(query)
print(results)

lat = results[0]['gemetry']['lat']
lng = results[0]['gemetry']['lng']

print(lat, lng)

myMap = folium.Map(location=[lat, lng], zoom_start = 9)

folium.Marker([lat, lng], popup=yourLocation).add_to(myMap)

# save map in html file
myMap.save("myLocation.html")
