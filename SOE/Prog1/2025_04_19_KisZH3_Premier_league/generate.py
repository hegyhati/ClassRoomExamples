import pandas as pd
import os, os.path
import json

basepath = "Premier_league"

df = pd.read_csv("dataset - 2020-09-24.csv")
for club, group in df.groupby("Club"):
    os.makedirs(os.path.join(basepath,club), exist_ok=True)
    for _, row in group.iterrows():
        if pd.notna(row['Jersey Number']):
            with open(os.path.join(basepath, club, f"{int(row['Jersey Number'])}_{row['Name'].split(' ')[-1]}_{row['Nationality']}.json"), 'w') as f:
                json.dump({
                "name" : row["Name"],
                "age" : row["Age"]
                }, f)