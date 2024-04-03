import pandas as pd
from read_csv import *

fish_df_cleaned = fish_df[fish_df['Weight'] != 0]

avg_species = fish_df_cleaned.groupby('Species').mean()
avg_species = avg_species.rename(columns={
    'Weight': 'Average Weight',
    'Length1': 'Average Length1',
    'Length2': 'Average Length2',
    'Length3': 'Average Length3',
    'Height': 'Average Height',
    'Width': 'Average Width'
})
