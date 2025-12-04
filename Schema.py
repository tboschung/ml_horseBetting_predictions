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