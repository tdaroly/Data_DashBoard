#data normalization
import pandas as pd
import numpy as np
df = pd.read_csv("C:\\Users\\taher\\OneDrive\\Desktop\\Work\\Chirality\\htmlDashBoards\\Data\\FracFocusRegistry_17.csv",dtype={"PercentHFJob": float,"IngredientComment":str,"PercentHighAdditive":float},low_memory=False)



df = df[df["Latitude"].between(-90,90,inclusive=False)]
grouped_df = df.groupby(by=["WellName","StateName","CountyName"]).aggregate(np.mean).dropna(axis=1, how='all')
grouped_df = grouped_df.reset_index()
lat = list(grouped_df["Latitude"])
lon = list(grouped_df["Longitude"])
well_names = list(grouped_df["WellName"])
