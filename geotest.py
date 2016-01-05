import googlemaps

# Input an address as a parameter, returns the latitude and longitude
def getCoordinates(address):
    gmaps = googlemaps.Client(key='AIzaSyCAdFRAtym1LwaUGHvmTb4ofnvgyrMDINA')
    geocode_result = gmaps.geocode(address)
    # print geocode_result[0]['geometry']['location']
    result = ""
    result = result+str(geocode_result[0]['geometry']['location']['lat']) + ','
    result = result+str(geocode_result[0]['geometry']['location']['lng'])
    return result
    

def getClosest(origin, destination,num):
    result = []
    counter = 0
    gmaps = googlemaps.Client(key='AIzaSyCAdFRAtym1LwaUGHvmTb4ofnvgyrMDINA')
    matrix = gmaps.distance_matrix(origin,destination,language="en",mode="walking")
    for i in matrix['rows']:
        for l in i['elements']:
            temp = []
            temp.append(l['distance']['value'])
            temp.append(l['duration']['text'])
            temp.append(destination[counter])

            counter = counter + 1
            result.append(temp)
    result = sorted(result)
    counter = 0
    topnum = []
    while (counter < num):
        topnum.append(result[counter])
        counter = counter + 1
    return topnum
        
        
    
print getClosest(["345 Chambers St, NY, 10282"],["Las Vegas","Grand Central Station", "Flushing, Queens","Los Angeles"],3)

# print getCoordinates('345 Chambers St, NY, 10282')

# geometry
# address_components
# place_id
# formatted_address
# types

        
