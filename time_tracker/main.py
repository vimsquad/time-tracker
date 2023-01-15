from datetime import datetime
from .data_store import DataStoreController, DataStore
from .schemas import TimeRow, TimeRecord, TimeStatus, TimeCategories


class AddEntry:
    """Adds A time Entry"""


class TimeTracker:
    """Tracks Time"""

    data_store: DataStore

    def __init__(self, data_store_type: str = "json"):
        self.data_store = DataStoreController.get_factory(
            data_store_type=data_store_type
        )
        self.data_store.create_data_store()

    def add_entry(self, description: str, category: str, status: str):
        """Adds Entry to data store"""
        now = datetime.now()  # current date and time
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

        self.data_store.upsert_data(
            description=description,
            data_to_write=TimeRow(
                time_record=TimeRecord(start_time=date_time),
                category=TimeCategories(category),
                status=TimeStatus(status),
            ),
        )
