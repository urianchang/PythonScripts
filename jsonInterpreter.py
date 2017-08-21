'''
What this script does:
    1. Make an API GET request
    2. Parse response as JSON
    3. Pretty print the JSON
'''

import requests
import json

URL = "http://cs.stage.int.sightmachine.com/v1/datatab/cycle?asset_selection=%7B%22machine_source%22%3A%5B%22CS_QD_StockFit_1%22%5D%7D"
cookie = {'session' : 'eyJfZnJlc2giOnRydWUsIl9pZCI6eyIgYiI6Ill6ZzNZVGMwTkRKaFltRXpOVGRpTVRrMVpXVmxORGRsWldVek9UQTBNams9In0sInVzZXJfaWQiOiI1NTVmZGNjMTc1NzNmMTZiOWNjOGI4OWMifQ.DHzTuA.GtvZRA6FzqJaJ-9Ngkusjvr8fOk'}

# URL = "http://pokeapi.co/api/v2/pokemon/4/"
r = requests.get(url=URL, cookies=cookie)
jsonResponse = r.json()

print json.dumps(jsonResponse, indent=2)
