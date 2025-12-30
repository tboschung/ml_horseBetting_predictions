import Utility
import Schema
import ast
import pandas as pd

filepath = "data/id_calendar.csv"
df = pd.read_csv(filepath)
df["race_ids"] = df["race_ids"].apply(ast.literal_eval)
df = df[df['year'] == 2025]
df = df[df['month'] == 1]

races = []
all_entries = []
all_odds = []
for index, row in df.iterrows():
    year = row["year"]
    month = row["month"]
    ids = row["race_ids"]

    print(f"{year}, {month}")
    for id in ids:
        race, entries = Utility.get_entry(id)
        _, result = Utility.get_result(id)
        odds = Utility.get_odds(id)
        for odd in odds:
            print(odd)
            all_odds.append(Schema.Odd(odd))
        races.append(Schema.RaceData(race[0]))
        print(races)
        break
    break


