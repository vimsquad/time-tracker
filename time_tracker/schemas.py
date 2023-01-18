import datetime
from dataclasses import dataclass
from enum import Enum, unique
from dataclasses_json import dataclass_json


@unique
class TimeCategories(str, Enum):
    project: str = "project"
    chat: str = "chat"
    meeting: str = "meeting"


@unique
class TimeStatus(str, Enum):
    completed: str = "completed"
    paused: str = "paused"
    cancelled: str = "cancelled"
    started: str = "started"


@dataclass()
class TimeRecord:
    start_time: datetime.datetime = ""
    end_time: datetime.datetime = ""


@dataclass_json
@dataclass()
class TimeRow:
    time_record: TimeRecord
    category: TimeCategories
    status: TimeStatus
