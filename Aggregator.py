import Utility
import Schema
import ast
import pandas as pd

filepath = "data/id_calendar.csv"
df = pd.read_csv(filepath)
df["race_ids"] = df["race_ids"].apply(ast.literal_eval)
df = df[df['year'] == 2025]
df = df[df['month'] == 1]

def build_odd_list(odds):
    all_odds = []
    for odd in odds:
        all_odds.append(Schema.Odd(odd))
    return all_odds

def build_entry_list(entries, results):
    all_entries = []
    merged = pd.merge( pd.DataFrame(entries), pd.DataFrame(results), on='id', how='inner')
    for _, row in merged.iterrows():
        all_entries.append(Schema.Entry(row))
    return all_entries

races = []
for index, row in df.iterrows():
    year = row["year"]
    month = row["month"]
    ids = row["race_ids"]

    print(f"{year}, {month}")
    for id in ids:
        raceData, entries = Utility.get_entry(id)
        _, results = Utility.get_result(id)
        odds = Utility.get_odds(id)
        race = Schema.Race(Schema.RaceData(raceData[0]), build_entry_list(entries, results), build_odd_list(odds))
        races.append(race)
        print(race)
        break
    break
