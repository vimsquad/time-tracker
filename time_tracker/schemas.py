import datetime
from dataclasses import dataclass
from enum import Enum
from typing import List
from dataclasses_json import dataclass_json


class TimeCategories(Enum):
    project: 0
    chat: 1
    meeting: 2


class TimeStatus(Enum):
    completed: 0
    paused: 1
    cancelled: 3
    started: 4


@dataclass()
class TimeRecord:
    start_time: datetime.datetime
    end_time: datetime.datetime = ""


@dataclass_json
@dataclass()
class TimeRow:
    time_record: TimeRecord
    category: TimeCategories
    status: TimeStatus
