import requests, json, sys
# secret contains API Key.  Not in Github repo !
# expects  AuthCode='API Key obtained from Thingful'
# see
# https://growobservatory.github.io/ThingfulNode/#
# how to get a Key
from Secret import AuthCode

url = "https://grow.thingful.net/api/entity/locations/get"
headers = {"Authorization": "Bearer {0}".format(AuthCode)}
payload = json.dumps({'DataSourceCodes': ['Thingful.Connectors.GROWSensors'] })

response = requests.post(url, headers=headers, data=payload)

jResp = response.json()

# exit if status code is not ok
if response.status_code != 200:
  print("Unexpected response: {0}. Status: {1}. Message: {2}".format(response.reason, response.status, jResp['Exception']['Message']))
  sys.exit()

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