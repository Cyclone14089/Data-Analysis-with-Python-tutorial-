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

print(indian_forwards[indian_forwards['name'].str.contains('Singh')])