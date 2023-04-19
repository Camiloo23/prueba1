import json 
import yaml

with open("myfile.json", "r") as json_file:
	ourjson = json.load(json_file)

print ("Su token es: {}".format(ourjson['access_token']))
print ("Su token vence en: {} second.".format(ourjson['expires_in']))
