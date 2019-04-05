import json

with open('/run/dump1090-mutability/aircraft.json') as airplanejson:
  data = json.load(airplanejson)
  
print len(data['aircraft'])
