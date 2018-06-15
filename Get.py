"""
This code reads from the Thingful node and gets a list of all Sensors.
The code then reads through the list of sensors and counts the number 
with a location of zero (at the moment assumes if x=0 y=0). Then displays 
percentage that are zero locations. 
Documentation for the GROW node is available at: 
https://growobservatory.github.io/ThingfulNode/#tag/Locations
"""

import requests
import json
import sys

# ensure the key has been passed as argument
try:
    api_key = sys.argv[1]
except:
    sys.exit("The API key must be passed as argument when executing the script. Please run 'python Get.py <your-api-key>'.")

url = "https://grow.thingful.net/api/entity/locations/get"
headers = {"Authorization": "Bearer {0}".format(api_key)}
payload = json.dumps({'DataSourceCodes': ['Thingful.Connectors.GROWSensors'] })

response = requests.post(url, headers=headers, data=payload)

jResp = response.json()

# exit if status code is not ok
if response.status_code != 200:
    sys.exit("Unexpected response: {0}. Status: {1}. Message: {2}".format(response.reason, response.status_code, jResp['Exception']['Message']))

#print json.dumps(jResp,indent=4,sort_keys=True)
#for key in jResp.items():
#    print key
#    print
#print jResp["Locations"]

Locations = jResp["Locations"]
numSensor=len(Locations)
print("Number of Sensors : {0}".format(numSensor))

xCount=0
yCount=0
Count=0
for thing in Locations:
    # print thing
    th=Locations[thing]
    x=th["X"]
    y=th["Y"]

    # print json.dumps(th,indent=4,sort_keys=True)
    # print x,y
    if (x==0):
        xCount+=1
    if (y==0):
        yCount+=1
    if ((x==0) and (y==0)):
        Count+=1

Percent= float(xCount)/float(numSensor)*100
print("Blanks Total {0} | x-coord {1} | y-coord {2} | Percentage Blank {3}".format(Count, xCount, yCount, Percent))
