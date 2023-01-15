from .data_store import DataStoreController


class TimeTracker:
    """Tracks Time"""

    def __init__(self):
        data_store = DataStoreController.get_factory(data_store_type="json")
        data_store.create_data_store()
