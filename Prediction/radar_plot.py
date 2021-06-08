import pandas as pd
import numpy as np
from copy import deepcopy
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

isl_df = pd.read_csv("~/Desktop/Football Data Analysis/Prediction/isl_player_final.csv")

indian_forwards = deepcopy(isl_df[(isl_df['country_id'] == 1) & (isl_df['position_id'] == 2) & (isl_df['minutes_played'] > 0)])
indian_forwards.reset_index(drop = True, inplace = True)

cols_for_per90 = ['events.goals', 'events.assists', 'events.shots', 'events.shots_on_target', 'events.chances_created', 'events.fouls_suffered', 'touches.total', 'touches.aerial_duel.won', 'touches.ground_duel.won']
per90_cols = [i + "_per90" for i in cols_for_per90]

# creating per90 columns :-
for k in range(0, len(per90_cols)):
    indian_forwards[per90_cols[k]] = indian_forwards[cols_for_per90[k]].divide(indian_forwards['minutes_played']).multiply(90)

# print(indian_forwards.loc[(indian_forwards['id'] == 19150), per90_cols].sum())

fig = px.line_polar(indian_forwards, r = indian_forwards.loc[(indian_forwards['id'] == 19150), per90_cols].sum(), theta = per90_cols, line_close = True)
fig.update_traces(fill = 'toself')
fig.show()

######    Normalisation of values    #####

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
indian_forwards[per90_cols] = scaler.fit_transform(indian_forwards[per90_cols])

# same radar plot after normalisation of the data
fig = px.line_polar(indian_forwards, r = indian_forwards.loc[(indian_forwards['id'] == 19150), per90_cols].sum(), theta = per90_cols, line_close = True)
fig.update_traces(fill = 'toself')
fig.show()