# This code reads from the Thingful node, gets  list of all Sensors
# The code then reads through the list of sensors and counts the number with a location of
# zero (at the moment assumes if x=0 y=0)
# Then displays percentage that are zero locations
# Documentation for GROW node
# https://growobservatory.github.io/ThingfulNode/#tag/Locations
#
#
#

import httplib,json
# secret contains API Key.  Not in Github repo !
# expects  AuthCode='API Key obtained from Thingful'
# see  
# https://growobservatory.github.io/ThingfulNode/#
# how to get a Key
from Secret import *
c = httplib.HTTPSConnection("grow.thingful.net")

headers = {'Authorization': 'Bearer %s' % AuthCode}
params = json.dumps({'DataSourceCodes': ['Thingful.Connectors.GROWSensors'] })

c.request("POST", "/api/entity/locations/get", params, headers)

response = c.getresponse()
print response.status, response.reason
jResp=json.loads(response.read())
#print json.dumps(jResp,indent=4,sort_keys=True)
#for key in jResp.items():
#    print key
#    print
#print jResp["Locations"]

Locations = jResp["Locations"]
numSensor=len(Locations)
print "Number of Sensors : %d" % numSensor
xCount=0;
yCount=0;
for thing in Locations:
#        print thing
        th=Locations[thing]
        x=th["X"]
        y=th["Y"]
#        print json.dumps(th,indent=4,sort_keys=True)
#        print x,y
        if (x==0):
           xCount+=1
        if (y==0):
           yCount+=1
print "Blanks",xCount,yCount
Percent= float(xCount)/float(numSensor)
print "Percent Blank", Percent
