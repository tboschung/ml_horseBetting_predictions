from dataclasses import dataclass
from datetime import date, time

@dataclass
class RaceData:
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

    def __init__(self, entry_data):
        self.id = entry_data["id"]
        
        self.race_id = entry_data["race_id_x"]
        self.bracket = entry_data["bracket_x"]
        self.horse_number = entry_data["horse_number_x"]

        self.horse_id = entry_data["horse_id_x"]
        self.horse_name = entry_data["horse_name_x"]
        self.gender = entry_data["gender_x"]
        self.age = entry_data["age_x"]

        self.burden = entry_data["burden_x"]

        self.jockey_id = entry_data["jockey_id_x"]
        self.jockey_name = entry_data["jockey_name_x"]
        self.trainer_id = entry_data["trainer_id_x"]
        self.trainer_name = entry_data["trainer_name_x"]

        self.weight = entry_data["weight_x"]
        self.weight_diff = entry_data["weight_diff_x"]

        # results data
        self.rank = entry_data["rank"]
        self.rap_time = entry_data["rap_time"]
        self.diff_time = entry_data["diff_time"]
        self.passage_rank = entry_data["passage_rank"]
        self.last_3f = entry_data["last_3f"]
        self.prize = entry_data["prize"]


@dataclass
class Odd:
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


@dataclass
class Race:
    raceData: RaceData
    entries: list[Entry]
    odds: list[Odd]
    
    def __init__(self, raceData, entries, odds):
        self.raceData = raceData
        self.entries = entries
        self.odds = odds
