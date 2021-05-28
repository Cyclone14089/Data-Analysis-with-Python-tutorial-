import pandas as pd
from bs4 import BeautifulSoup
import json
from urllib.request import urlopen

url = "https://understat.com/league/EPL"

dom = BeautifulSoup(urlopen(url), "html.parser") # imports the document-object-model of the webpage

def get_json_data(dom):

    all_data_inside_scripts = dom.findAll(name="script") # returns an object containing all everything under every 'script' tag
    print(type(all_data_inside_scripts))

    player_data = all_data_inside_scripts[3] # the third index of the object contains 'player_data'
    # print(type(player_data))
    # print(player_data)

    player_data = str(player_data) # converting it into string type
    # print(type(player_data))
    # print(player_data)

    # we need to slice the string to strip out unwanted data
    start_index = player_data.index("('") + 2
    end_index = player_data.index("')")
    player_data = player_data[start_index:end_index]

    # now, we will convert it to json format and strip it further to remove all unwanted data
    json_data = player_data.encode("utf-8").decode("unicode-escape")

    return json_data # returns a string in json format


json_df = pd.json_normalize(json.loads(get_json_data(dom))) # converting json into data frame

print(json_df) # printing the data frame

print(json_df.columns, "\n") # printing the column names

print(json_df[["player_name", "games", "time", "goals", "team_title"]]) # printing certain columns

print(json_df.info()) # printing basic information about the data frame