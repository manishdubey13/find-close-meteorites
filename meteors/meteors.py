import requests
import math


def calc_distance(lat1,log1,lat2,log2):
    lat1=math.radians(lat1)
    log1=math.radians(log1)
    lat2=math.radians(lat2)
    log2=math.radians(log2)

    h=math.sin((lat2-lat1)/2)**2 + math.cos(lat1)*math.cos(lat2)*math.sin((log2-log1)/2)**2

    return 6372.8 * 2 *math.asin(math.sqrt(h))

def get_distance(meteor):
    return meteor.get('distance',math.inf)

res=requests.get("http://nasa.gov")


text = res.text

meteors_res=requests.get("https://data.nasa.gov/resource/gh4g-9sfh.json")
meteors_data = meteors_res.json()

if __name__=='__main__':
    my_location =(22.095598,79.556060)

    for meteor in meteors_data:
        if not('reclat' in meteor and 'reclong' in meteor): continue
        meteor['distance']=calc_distance(float(meteor['reclat']),float(meteor['reclong']),my_location[0],my_location[1])

    meteors_data.sort(key=get_distance)


    withno_distance= len([m for m in meteors_data if 'distance' not in m])


    for m in meteors_data[0:10]:
        lat=m['reclat']
        long=m['reclong']
        url="https://maps.google.com/?q="
        final_url=f'{url}{lat},{long}'
        print("For My Place to Meteorite Site in  " + m['name'] +  "  is    "  + str(m['distance']) +" Mile. far, in year "+
              str(m['year']) + " and google map location is  "+ final_url)

