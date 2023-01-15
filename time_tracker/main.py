from datetime import datetime
from .data_store import DataStoreController
from .schemas import TimeRow, TimeRecord


class TimeTracker:
    """Tracks Time"""

    def __init__(self):
        data_store = DataStoreController.get_factory(data_store_type="json")
        data_store.create_data_store()
        now = datetime.now()  # current date and time
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

        data_store.upsert_data(
            description="test",
            data_to_write=TimeRow(
                time_record=TimeRecord(start_time=date_time),
                category="meeting",
                status="started",
            ),
        )
