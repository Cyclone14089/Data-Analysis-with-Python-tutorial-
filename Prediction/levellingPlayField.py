import pandas as pd
import numpy as np
from copy import deepcopy
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

isl_df = pd.read_csv("~/Desktop/Football Data Analysis/Prediction/isl_player_final.csv") # reading the file and storing it

# print(isl_df.info())

# print(isl_df.describe().round(1))

# print(isl_df[(isl_df['minutes_played'] > 1500) & (isl_df['country_id'] == 1)].shape)

# print(isl_df[(isl_df['country_id'] == 1) & (isl_df['position_id'] == 2)])

indian_forwards = deepcopy(isl_df[(isl_df['country_id'] == 1) & (isl_df['position_id'] == 2)])

indian_forwards.reset_index(drop = True, inplace = True)
# print(indian_forwards)

# print(indian_forwards[indian_forwards['name'].str.contains('Singh')])


#####  Level the Playing Field  #####

fwd_min_df = indian_forwards.groupby(['id', 'name'])['minutes_played'].sum().reset_index()
# print(fwd_min_df)

fig = px.bar(x = 'name', y = 'minutes_played', data_frame = fwd_min_df)
# fig.show()

# print(fwd_min_df[['name', 'minutes_played']])

# print(fwd_min_df['name'].to_list())
# print(fwd_min_df['minutes_played'].to_list())

# x_axis = fwd_min_df['name'].to_list()
# y_axis = fwd_min_df['minutes_played'].to_list()

# plt.bar(x_axis, y_axis)
# plt.xticks(x_axis, rotation = 30)
# plt.show(block=True)



#####  Calculating per 90 stats  #####

indian_forwards = indian_forwards[indian_forwards['minutes_played'] > 0] # eliminate stats of players who played <= 0 minutes

# create a list of columns whose 'per 90' stats are to be calculated
cols_for_per90 = ['events.goals', 'events.assists', 'events.shots', 'events.shots_on_target', 'events.chances_created', 'events.fouls_suffered', 'touches.total', 'touches.aerial_duel.won', 'touches.ground_duel.won']

per90_cols = [i + "_per90" for i in cols_for_per90] # creating list of per 90 cols

# creating per90 columns :-
for k in range(0, len(per90_cols)):
    indian_forwards[per90_cols[k]] = indian_forwards[cols_for_per90[k]].divide(indian_forwards['minutes_played']).multiply(90)

per90_df = indian_forwards[per90_cols]
# print(per90_df)

# per90_df.to_csv('per90.csv', sep = '\t') # dumping the data frame into a csv file


#####  Multiple players  #####

# for i, row in indian_forwards.iterrows():
    # print("Index location -->", i, "\n")
    # print(row.values, "\n")

    # print(row['name'])
    # fig = px.line_polar(indian_forwards, r = indian_forwards.loc[(indian_forwards['id'] == row['id']), cols_for_per90].sum(), theta = cols_for_per90, line_close = True)
    # fig.update_traces(fill = 'toself')
    # fig.show()

for i, row in indian_forwards.iterrows():
    # print(indian_forwards.loc[(indian_forwards['id'] == row['id'])])
    print(i, row)

# fig = px.line_polar(indian_forwards, r = indian_forwards.loc[0, cols_for_per90].sum(), theta = cols_for_per90, line_close = True)
# fig.update_traces(fill = 'toself')
# fig.show()