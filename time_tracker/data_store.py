import os
from abc import ABC, abstractmethod
import json
from os import path
from .schemas import TimeRow, TimeRecord
from datetime import datetime


class DataStore(ABC):
    """Stores Data in persistent storage"""

    @abstractmethod
    def get_current_time(self):
        """Gets Current Time"""
        pass

    @abstractmethod
    def create_data_store(self):
        """Creates Data Store If not Exists"""
        pass

    @abstractmethod
    def add_time_entry(self, description: str, data_to_write: TimeRow) -> bool:
        """Updates or Inserts Data"""
        pass

    @abstractmethod
    def modify_time_entry(self):
        """Adjusts Time entry"""
        pass

    @abstractmethod
    def delete_time_entry(self):
        """Deletes Data"""
        pass

    @abstractmethod
    def load_data(self):
        """Loads data from datastore"""
        pass

    @abstractmethod
    def persist_data(self):
        """Persist datastore"""
        pass


class DataStoreJson(DataStore):
    """Stores Data in persistent storage"""

    date_format = "%m/%d/%Y %H:%M:%S"
    data_location: str = "time_tracker_data_store.json"
    loaded_data: dict = {}

    def get_current_time(self):
        """Gets Current Time"""
        now = datetime.now()
        return now.strftime(self.date_format)

    def create_data_store(self):
        """Creates Data Store If not Exists"""
        if not path.exists(f"{os.getenv('HOME')}/{self.data_location}"):
            with open(f"{os.getenv('HOME')}/{self.data_location}", "w") as outfile:
                outfile.write(json.dumps({}))
        self.load_data()

    def add_time_entry(self, description: str, data_to_write: TimeRow):
        """Updates or Inserts Data"""
        if description in self.loaded_data.keys():
            self.upsert_data(description=description, data_to_write=data_to_write)
        else:
            if data_to_write.status == "started":
                data_to_write.time_record.start_time = self.get_current_time()
            self.loaded_data[description] = data_to_write.to_dict()

        self.persist_data()

    def upsert_data(self, description: str, data_to_write: TimeRow):
        """Upserts Data"""
        if data_to_write.status != "started":
            data_to_write.time_record = TimeRecord(
                start_time=self.loaded_data[description]["time_record"]["start_time"],
                end_time=self.get_current_time(),
            )
            self.loaded_data[description] = data_to_write.to_dict()

    def modify_time_entry(self):
        """Adjusts Time entry"""
        pass

    def delete_time_entry(self):
        """Deletes Data"""
        pass

    def load_data(self):
        """Loads data from datastore"""
        with open(f"{os.getenv('HOME')}/{self.data_location}", "r") as outfile:
            self.loaded_data = json.load(outfile)

    def persist_data(self):
        """Persist datastore"""
        with open(f"{os.getenv('HOME')}/{self.data_location}", "w") as outfile:
            outfile.write(json.dumps(self.loaded_data))


class DataStoreController:
    """Gets DataStore"""

    @staticmethod
    def get_factory(data_store_type: str = "json") -> DataStore:
        factories = {"json": DataStoreJson()}
        return factories.get(data_store_type)
