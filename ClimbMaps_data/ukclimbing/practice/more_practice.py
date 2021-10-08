import os
import sys
import json
with open(os.path.join(sys.path[0], "alfordpractice.json"), "r") as f:
    data = f.read()

listed = json.loads(data)
for x in listed:
    print((x['Area Name:']),'      ', x['Coordinates:'])
