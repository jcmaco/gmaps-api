import googlemaps
from datetime import datetime
import pprint

pp = pprint.PrettyPrinter(indent=4)

gmaps = googlemaps.Client(key='YOUR_API_KEY')


def journeyTime(a):
##    pp.pprint(a)
    for j in range(len(origins)):
        origin=origins[j]
        time = 0
        for i in range(len(destinations)):
            time += a["rows"][j]["elements"][i]["duration"]["value"]
        print('Total journey time from {0} by {1} is {2:.1f} mins'.format(origin,mode,time/60))
        timeOrigin[j] += time
    print('')


origins=["Carlton North, Melbourne",
         "Brunswick East, Melbourne",
         "Richmond, Melbourne",
         "Fritzroy, Melbourne",
         "Collingwood, Melbourne"]

timeOrigin = [0]*len(origins)


destinations=["Melbourne Airport",
              "Grampians National Park"]
mode="driving"
journeyTime(gmaps.distance_matrix(origins, destinations, mode=mode))

destinations=["Queen Vicotria Market, Melbourne",
              "North Walls, Melbourne",
              "Royal Park, Melbourne"]
mode="bicycling"
journeyTime(gmaps.distance_matrix(origins, destinations, mode=mode))

destinations=["Collins St, Melbourne"]
mode="transit"
journeyTime(gmaps.distance_matrix(origins, destinations, mode=mode))

for i in range(len(origins)):
    print('Grand total journey time from {0} is {1:.1f} mins'.format(origins[i],[x / 60 for x in timeOrigin][i]))
    
