import json
import yaml

with open ('/home/devasc/labs/devnet-src/parsing/myfile.json','r')as json_file:
    ourjson = json.load (json_file)
print(ourjson)
print("the access token is : {}".format(ourjson['access_token']))
print("The token expires in: {} seconds". format(ourjson['expires_in']))
