import requests
import math


res=requests.get("http://nasa.gov")

print(res.status_code)

text = res.text

#print(text)

print(len(text))

meteors_res=requests.get("https://data.nasa.gov/resource/gh4g-9sfh.json")
meteors_data = meteors_res.json()
print(type(meteors_data))
print(meteors_data[0])

####https://www.findlatitudeandlongitude.com/
#####https://www.geeksforgeeks.org/program-distance-two-points-earth/#:~:text=For%20this%20divide%20the%20values,is%20the%20radius%20of%20Earth.
##Distance betweemn two points give there latitude and longitude
# Haversine formula


def calc_distance(lat1,log1,lat2,log2):
    lat1=math.radians(lat1)
    log1=math.radians(log1)
    lat2=math.radians(lat2)
    log2=math.radians(log2)

    h=math.sin((lat2-lat1)/2)**2 + math.cos(lat1)*math.cos(lat2)*math.sin((log2-log1)/2)**2

    return 6372.8 * 2 *math.asin(math.sqrt(h))

my_location =(22.095598,79.556060)

# print ( " Distance form my place is " + str( calc_distance(50.775000,6.083330,my_location[0],my_location[1])))

###distance between my place and all the places having latitude and longitude data

for meteor in meteors_data:
    if not('reclat' in meteor and 'reclong' in meteor): continue
    meteor['distance']=calc_distance(float(meteor['reclat']),float(meteor['reclong']),my_location[0],my_location[1])


# print("Before  sort" + str(meteors_data[0]) )
def get_distance(meteor):
    return meteor.get('distance',math.inf)

meteors_data.sort(key=get_distance)

# print("After  sort" + str(meteors_data[0]) )

##print("Nearest 10 from Seoni "+ str(meteors_data[0:10]))

##find out how many with no distance

withno_distance= len([m for m in meteors_data if 'distance' not in m])

##print("With no distance "+ str(withno_distance))

##sorted_meteors_data =meteors_data.sort(key=get_distance)

#
# for me in sorted_meteors_data:
#     if not( 'distance' in me) :continue
#     print(me)



####
##https://maps.google.com/?q=25.25417,80.625

for m in meteors_data[0:10]:
    lat=m['reclat']
    long=m['reclong']
    url="https://maps.google.com/?q="
    final_url=f'{url}{lat},{long}'
    print("For My Place to Meteorite Site in  " + m['name'] +  "  is    "  + str(m['distance']) +" Mile. far, in year "+
          str(m['year']) + " and google map location is  "+ final_url)



