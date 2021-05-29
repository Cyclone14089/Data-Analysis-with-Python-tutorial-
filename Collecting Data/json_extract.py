import requests
import json

url = "https://api.sofascore.com/api/v1/unique-tournament/1900/season/34713/standings/total"

response = requests.get(url) # storing response recieved via get request to the api url
content = response.content # storing the content of the request
json_object = json.loads(content)

print(response) # must print the value '200', which is http code for 'OK'

with open('json_content.txt', 'w') as content_store:
    json.dump(json_object, content_store)

print(json_object)