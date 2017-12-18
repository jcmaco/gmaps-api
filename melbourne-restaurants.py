import googlemaps
from datetime import datetime
import pprint
import time
import sys

pp = pprint.PrettyPrinter(indent=4)

gmaps = googlemaps.Client(key='YOUR_API_KEY')

origins=["Carlton North, Melbourne",
         "Brunswick East, Melbourne",
         "Richmond, Melbourne",
         "Fritzroy, Melbourne",
         "Collingwood, Melbourne"]

for origin in origins:
    a = gmaps.geocode(address=origin)
    coord = a[0]['geometry']["location"]
    coord = [coord["lat"],coord["lng"]]
    coord = '{},{}'.format(coord[0],coord[1])
    b = gmaps.places_nearby(location=coord, radius=500, type="restaurant")
    
    c={'results':[]} #initialise empty results vars in case more than 20 results
    d={'results':[]}

    
    if b.get('next_page_token'):
        next_page_token = b['next_page_token']
        try:
            time.sleep(2) # Next page is not immediately available
            c = gmaps.places_nearby(location=coord, page_token=next_page_token)
        except:
            print('Warning: next page was not available. Retrying now.')
            print("Unexpected error:", sys.exc_info()[0])
            time.sleep(2)
            c = gmaps.places_nearby(location=coord, page_token=next_page_token) 

    if c.get('next_page_token'):
        next_page_token = c['next_page_token']
        try:
            time.sleep(2)
            d = gmaps.places_nearby(location=coord, page_token=next_page_token)
        except:
            print('Warning: next page was not available. Retrying now.')
            print("Unexpected error:", sys.exc_info()[0])
            time.sleep(2)
            d = gmaps.places_nearby(location=coord, page_token=next_page_token)


    ##pp.pprint(b)
    ##pp.pprint(c)
    ##pp.pprint(d)

    results = b['results'] + c['results'] + d['results']

    print(origin, ': ', len(results), 'Google Maps results')
    good = []
    for i in results:
        try:
            if i['rating'] >= 4.5:
                print('{0:.1f} {1}'.format(i['rating'],i['name']))
                good.append(i)

        except:
                pass
    print(origin, ': ', len(good), 'good restaurants\n')

