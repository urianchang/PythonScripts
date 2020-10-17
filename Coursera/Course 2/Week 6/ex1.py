import urllib
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
#    print 'Retrieving...', url
    uh = urllib.urlopen(url)
    data = uh.read()
#    print 'Retrieved',len(data),'characters!'

    try: js = json.loads(str(data))
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print '==== Failure To Retrieve ===='
        print data
        continue

#    print json.dumps(js, indent=4)
    try: 
        if js['results'][0]['address_components'][0]['types'] == ['country', 'political'] : 
            cc = js['results'][0]['address_components'][0]['short_name']
            print 'Country Code is:', cc
        elif js['results'][0]['address_components'][1]['types'] == ['country', 'political'] : 
            cc = js['results'][0]['address_components'][1]['short_name']
            print 'Country Code is:', cc
        elif js['results'][0]['address_components'][2]['types'] == ['country', 'political'] : 
            cc = js['results'][0]['address_components'][2]['short_name']
            print 'Country Code is:', cc
        elif js['results'][0]['address_components'][3]['types'] == ['country', 'political'] : 
            cc = js['results'][0]['address_components'][3]['short_name']
            print 'Country Code is:', cc   
        elif js['results'][0]['address_components'][4]['types'] == ['country', 'political'] : 
            cc = js['results'][0]['address_components'][4]['short_name']
            print 'Country Code is:', cc
        elif js['results'][0]['address_components'][5]['types'] == ['country', 'political'] : 
            cc = js['results'][0]['address_components'][5]['short_name']
            print 'Country Code is:', cc
        elif js['results'][0]['address_components'][6]['types'] == ['country', 'political'] : 
            cc = js['results'][0]['address_components'][6]['short_name']
            print 'Country Code is:', cc    
    except: 
        print 'There is no Country Code.'
        
#    lat = js["results"][0]["geometry"]["location"]["lat"]
#    lng = js["results"][0]["geometry"]["location"]["lng"]
#    print 'lat',lat,'lng',lng
#    location = js['results'][0]['formatted_address']
#    print location

