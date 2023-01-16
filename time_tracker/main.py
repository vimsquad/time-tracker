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

        self.data_store.add_time_entry(
            description=description,
            data_to_write=TimeRow(
                time_record=TimeRecord(),
                category=TimeCategories(category),
                status=TimeStatus(status),
            ),
        )
