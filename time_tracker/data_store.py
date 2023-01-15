import os
from abc import ABC, abstractmethod
import json
from os import path
from .schemas import TimeRow


class DataStore(ABC):
    """Stores Data in persistent storage"""

    @abstractmethod
    def create_data_store(self):
        """Creates Data Store If not Exists"""
        pass

    @abstractmethod
    def upsert_data(self, description: str, data_to_write: TimeRow) -> bool:
        """Updates or Inserts Data"""
        pass

    @abstractmethod
    def delete_data(self):
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

    data_location: str = "time_tracker_data_store.json"
    loaded_data: dict = {}

    def create_data_store(self):
        """Creates Data Store If not Exists"""
        if not path.exists(f"{os.getenv('HOME')}/{self.data_location}"):
            with open(f"{os.getenv('HOME')}/{self.data_location}", "w") as outfile:
                outfile.write(json.dumps({}))
        self.load_data()

    def upsert_data(self, description: str, data_to_write: TimeRow):
        """Updates or Inserts Data"""
        if description in self.loaded_data.keys():
            print("need upsert here")
        else:
            self.loaded_data[description] = data_to_write.to_dict()

        self.persist_data()

    def delete_data(self):
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
