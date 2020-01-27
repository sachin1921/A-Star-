import requests
import json
from time import sleep

f = open("elevation_data.py", "w+")
f.write("nodes = {\n")
for node in nodes:
    sleep(0.5)
    print(node["lat"])
    print(node["lng"])
    r = requests.get(f"http://elevation-api.io/api/elevation?points=({node['lat']},{node['lng']})")
    r = r.content.decode("utf-8")
    r = json.loads(r) 
    f.write(f"'{node['id']}': {r['elevations'][0]['elevation']},\n")
f.write("}")
