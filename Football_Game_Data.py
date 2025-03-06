import http.client
from pprint import PrettyPrinter
import json






conn = http.client.HTTPSConnection("v3.football.api-sports.io")



printer = PrettyPrinter()



headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': "45c778b9b09285810680af0866f0921f"
    }


conn.request("GET", "/countries", headers=headers)



res = conn.getresponse()
data = res.read()
info = json.loads(data)




printer.pprint(info['response'])






