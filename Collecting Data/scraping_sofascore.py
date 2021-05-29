import json

# check json_extract.py for the scraping

json_content_file = open('json_content.json')
json_string = json_content_file.read() # reading the json data and storing
json_object = json.loads(json_string) # storing the json string in dictionary
json_content_file.close()

print(len(json_object), end=",  ") # print the number of keys present
print(json_object.keys()) # print the keys present in the dictionary

print(json_object['standings'].__len__())
print([item.keys() for item in json_object['standings']])

print()

print(json.dumps(json_object['standings'][0]['tournament'], indent=3))

import pandas as pd

df = pd.json_normalize(json_object['standings'][0]['rows'])
print(df)
