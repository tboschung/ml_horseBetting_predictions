"""
Article 14 (Prohibition of Use Outside the Scope of Private Use)
1. Unless approved by the Company (the approval includes a User obtaining the consent of a third party via the Company if such third party holds rights to the relevant information ), a User may not use, for the purpose of reproduction, sale, or publication outside the scope of private use permitted under the Copyright Act, any data, information, text, remarks, software, etc., obtained through the Services (hereinafter collectively, “Data”). Even if such Data is not regarded as a work in the use of the Services, as long as such Data has been obtained through the Services, it shall be regarded as a work. Any act of placing Data in a condition in which an unspecified or large number of people are able to access it shall be regarded as an act of use that is outside the scope of private use, regardless of its objective.
2. A User may not have a third party perform any act that is in breach of the preceding paragraph.
"""

import json
import keibascraper
import pandas as pd

print("Script started")

# ==============================================
# =============== HELPER METHODS ===============

def array_to_csv(filepath, data):
    filepath = "data/id_calendar.csv"
    pd.DataFrame(data).to_csv(filepath, index=False)
    return

def file_exists(filepath):
    return Path(filepath).is_file()

def read_file(filepath):
    out_json = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            out_json.append(json.loads(line))
    return out_json

def write_file(input_json, filepath):
    with open(filepath, "a", encoding="utf-8") as f:
        for item in input_json:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")

def get_id_by_calendar(year_list, month_list = range(1,13)):
    all_race_ids = []
    for year in year_list:
        for month in month_list:
            race_ids = keibascraper.race_list(year, month)
            entry = {"year": year, "month": month, "race_ids": race_ids}
            all_race_ids.append(entry)
    return all_race_ids

def get_entry(id, dump_race=True, dump_entry=True):
    entry_filepath = f"data/entry/{id}_entry.ndjson"
    if file_exists(entry_filepath):
        entry = read_file(entry_filepath)
        race = read_file(f"data/race/{id}_race.ndjson")
        return race, entry
    race, entry = keibascraper.load("entry", str(id))
    if dump_race:
        write_file(race, f"data/race/{id}_race.ndjson")
    if dump_entry:
        write_file(entry, f"data/entry/{id}_entry.ndjson", )
    return race, entry

def get_result(id, dump_race=True, dump_result=True):
    result_filepath =  f"data/result/{id}_result.ndjson"
    if file_exists(result_filepath):
        result = read_file(result_filepath)
        race = read_file(f"data/race/{id}_race.ndjson")
        return race, result
    race, result = keibascraper.load("result", str(id))
    if dump_race:
        write_file(race, f"data/race/{id}_race.ndjson")
    if dump_result:
        write_file(result, f"data/result/{id}_result.ndjson", )
    return race, result

def get_odds(id, dump=True):
    odds_filepath = f"data/odds/{id}_odds.ndjson"
    if file_exists(odds_filepath):
        return read_file(odds_filepath)
    odds = keibascraper.load("odds", "201206050810")
    if dump:
        write_file(odds, f"data/odds/{id}_odds.ndjson")
    return odds

# ==============================================
# ================= DATA TYPES =================

from dataclasses import dataclass
from datetime import date, time

@dataclass
class Race:
    id: int
    number: int
    name: str
    date: date
    time: time
    type: str
    length: int
    length_class: str
    handed : str
    weather: str
    condition: str
    place: str
    course: str
    round: int
    days: int
    head_count: int
    max_prize: float
    """
    """
    def __init__(self, race_json):
        self.id = race_json["id"]
        self.number = race_json["race_number"]
        self.name = race_json["race_name"]
        self.date = race_json["race_date"]
        self.time = race_json["race_time"]
        self.type = race_json["type"]
        self.length = race_json["length"]
        self.length_class = race_json["length_class"]
        self.handed = race_json["handed"]
        self.weather = race_json["weather"]
        self.condition = race_json["condition"]
        self.place = race_json["place"]
        self.course = race_json["course"]
        self.round = race_json["round"]
        self.days = race_json["days"]
        self.head_count = race_json["head_count"]
        self.max_prize = race_json["max_prize"]

from dataclasses import dataclass

@dataclass
class Entry:
    id: str
    race_id: str
    bracket: int
    horse_number: int
    horse_id: str
    horse_name: str
    gender: str
    age: int
    burden: float

    jockey_id: str
    jockey_name: str
    trainer_id: str
    trainer_name: str

    weight: int
    weight_diff: int
    rank: int
    rap_time: float
    diff_time: float
    passage_rank: str
    last_3f: float
    prize: float

    def __init__(self, race_entry_json, result_entry_json):
        self.id = race_entry_json["id"]
        self.race_id = race_entry_json["race_id"]
        self.bracket = race_entry_json["bracket"]
        self.horse_number = race_entry_json["horse_number"]

        self.horse_id = race_entry_json["horse_id"]
        self.horse_name = race_entry_json["horse_name"]
        self.gender = race_entry_json["gender"]
        self.age = race_entry_json["age"]

        self.burden = race_entry_json["burden"]

        self.jockey_id = race_entry_json["jockey_id"]
        self.jockey_name = race_entry_json["jockey_name"]
        self.trainer_id = race_entry_json["trainer_id"]
        self.trainer_name = race_entry_json["trainer_name"]

        self.weight = race_entry_json["weight"]
        self.weight_diff = race_entry_json["weight_diff"]

        # results data
        self.rank = result_entry_json["rank"]
        self.rap_time = result_entry_json["rap_time"]
        self.diff_time = result_entry_json["diff_time"]
        self.passage_rank = result_entry_json["passage_rank"]
        self.last_3f = result_entry_json["last_3f"]
        self.prize = result_entry_json["prize"]


@dataclass
class Odds:
    race_id: str
    horse_number: int
    win: float
    show_min: float
    show_max: float

    def __init__(self, odds_json):
        self.race_id = odds_json["race_id"]
        self.horse_number = odds_json["horse_number"]
        
        self.win = odds_json["win"]
        self.show_min = odds_json["show_min"]
        self.show_max = odds_json["show_max"]


@dataclass
class HorseStats:
    horse_id: int
    year: int
    month: int
    races: list[int]
    num_races: int

    age: int
    avg_weight: float
    var_weight: float

    total_wins: int
    win_ratio: float
    average_rank: float

    total_wins: int
    win_ratio: float
    average_rank: float

@dataclass
class Horse:
    id: str
    horse_number: int
    gender: str
    cur_age: int
    jockeys: list[int] 
    trainers: list[int] 

    stats: list[HorseStats]

    def __init__(self, odds_json):
        self.id = odds_json.id
        self.race_id = odds_json.race_id
        self.horse_number = odds_json.horse_number

        self.win = odds_json.win
        self.show_min = odds_json.show_min
        self.show_max = odds_json.show_max


# ==============================================
# =================== ACTION ===================


# broken: 
#horse, result = keibascraper.load("horse", "2021190001")
# print(horse)
# print(result)

"""
5/2025
Failed to parse data for 202505021109: No valid data found for race with ID 202505021109
"""
import time
import ast
from pathlib import Path

def main():
    filepath = "data/id_calendar.csv"
    df = pd.read_csv(filepath)
    df["race_ids"] = df["race_ids"].apply(ast.literal_eval)
    df = df[df['year'] == 2025]

    for index, row in df.iterrows():
        time_month = time.time()
        year = row["year"]
        month = row["month"]
        if month in [1, 2, 3, 4]:
            continue
        ids = row["race_ids"]

        print(f"{year}, {month}")
        x = 0
        entry_time = time.time()
        for id in ids:
            my_file = Path(f"data/odds/{id}.ndjson")
            if my_file.is_file():
                print("skipping",id)
                continue
            x += 1
            if(x % 10 == 0):
                new_time = time.time()
                print(f"time for 10 ids: {new_time - entry_time}")
                entry_time = new_time
            try:
                race, entry = get_entry(id)
                _, result = get_result(id)
                odds = get_odds(id)
            except RuntimeError as e:
                print("\n" + 50*"=")
                print(e)
                print(50*"=" + "\n")
        print(f"{month}/{year} took {time.time()-time_month}")

if __name__ == "__main__":
    main()